import streamlit as st
import requests
import pandas as pd
import time

# --- CONFIGURATION ---
st.set_page_config(
    page_title="Bulk Ads.txt Scanner",
    layout="wide"
)

def format_url(input_line):
    """
    Cleans the input line to extract just the domain.
    """
    if not input_line:
        return None
    # Remove protocol
    clean = input_line.replace("https://", "").replace("http://", "")
    # Remove path
    clean = clean.split("/")[0]
    return clean.strip()

def check_single_domain(domain, filename):
    """
    Checks a single domain and returns a dictionary of results.
    """
    target_url = f"https://{domain}/{filename}"
    
    try:
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
        }
        
        response = requests.get(target_url, headers=headers, timeout=5)
        
        # Soft 404 check
        if response.status_code == 200:
            if "<html" in response.text.lower() or "<body" in response.text.lower():
                 return {
                    "Domain": domain,
                    "Status": "Soft 404",
                    "Code": 200,
                    "Lines": 0,
                    "URL": target_url
                }

            line_count = len(response.text.strip().split('\n'))
            return {
                "Domain": domain,
                "Status": "Found",
                "Code": 200,
                "Lines": line_count,
                "URL": target_url
            }
        else:
            return {
                "Domain": domain,
                "Status": "Missing/Error",
                "Code": response.status_code,
                "Lines": 0,
                "URL": target_url
            }
            
    except requests.exceptions.Timeout:
        return {"Domain": domain, "Status": "Timeout", "Code": 408, "Lines": 0, "URL": target_url}
    except requests.exceptions.ConnectionError:
        return {"Domain": domain, "Status": "Connection Error", "Code": 0, "Lines": 0, "URL": target_url}
    except Exception as e:
        return {"Domain": domain, "Status": "Error", "Code": 500, "Lines": 0, "URL": target_url}

# --- UI LAYOUT ---

st.title("Bulk Ads.txt Availability Scanner")
st.markdown("Batch check the existence and health of `ads.txt` or `app-ads.txt` files across multiple domains.")

# Sidebar Controls
with st.sidebar:
    st.header("Configuration")
    file_type = st.radio(
        "Target File:",
        ("ads.txt", "app-ads.txt")
    )

# Main Input Area
input_text = st.text_area(
    "Enter Domains (One per line)", 
    placeholder="cnn.com\nnytimes.com\nwsj.com",
    height=200
)

# Action Button
if st.button("Start Scan"):
    if not input_text.strip():
        st.warning("Please enter at least one domain.")
    else:
        # Prepare list
        raw_lines = input_text.split('\n')
        domains_to_check = []
        
        # Clean inputs
        for line in raw_lines:
            clean_d = format_url(line)
            if clean_d:
                domains_to_check.append(clean_d)
        
        # Remove duplicates
        domains_to_check = list(set(domains_to_check))
        
        if not domains_to_check:
            st.warning("No valid domains found.")
        else:
            results = []
            progress_bar = st.progress(0)
            status_text = st.empty()
            
            total = len(domains_to_check)
            
            # Processing Loop
            for i, domain in enumerate(domains_to_check):
                # Update UI
                status_text.text(f"Scanning {domain} ({i+1}/{total})...")
                progress_bar.progress((i + 1) / total)
                
                # Check Domain
                data = check_single_domain(domain, file_type)
                results.append(data)
                
                # Small sleep to be polite to APIs/Networks if checking hundreds
                time.sleep(0.1) 
            
            # Finalize
            progress_bar.empty()
            status_text.empty()
            
            # Create DataFrame
            df = pd.DataFrame(results)
            
            # --- RESULTS SECTION ---
            st.divider()
            st.subheader("Scan Results")
            
            # Summary Metrics
            found_count = len(df[df['Status'] == 'Found'])
            missing_count = len(df) - found_count
            
            m1, m2, m3 = st.columns(3)
            m1.metric("Total Scanned", total)
            m2.metric("Files Found", found_count)
            m3.metric("Missing / Errors", missing_count)
            
            # Display Table
            # Highlight 'Found' rows visually if possible, or just show data
            st.dataframe(
                df, 
                use_container_width=True,
                column_config={
                    "URL": st.column_config.LinkColumn("File Link")
                }
            )
            
            # CSV Download
            csv_data = df.to_csv(index=False).encode('utf-8')
            st.download_button(
                label="Download Report (CSV)",
                data=csv_data,
                file_name=f"ads_scan_results_{file_type}.csv",
                mime='text/csv'
            )
