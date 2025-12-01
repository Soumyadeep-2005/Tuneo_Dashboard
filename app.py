import streamlit as st
import pandas as pd
import plotly.express as px


st.set_page_config(page_title="Tune Dashboard – JioSaavn & Wynk", layout="wide", initial_sidebar_state="expanded")

# Custom CSS - Single clean background color across entire page
# NOTE: change #f4f5fb to another hex if I want a different global background color.
st.markdown("""
<style>
    /* Hide default Streamlit elements */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    
    /* === GLOBAL PAGE BACKGROUND === */
    html, body {
        background-color: #f4f5fb !important;
        background: #f4f5fb !important;
    }
    
    /* Full page background coverage */
    #root {
        background-color: #f4f5fb !important;
        background: #f4f5fb !important;
    }
    
    .stApp {
        background-color: #f4f5fb !important;
        background: #f4f5fb !important;
    }
    
    [data-testid="stAppViewContainer"] {
        background-color: #f4f5fb !important;
        background: #f4f5fb !important;
    }
    
    [data-testid="stAppViewContainer"] > div {
        background-color: #f4f5fb !important;
        background: #f4f5fb !important;
    }
    
    [data-testid="stSidebar"] {
        background-color: #eef0f8 !important;
        background: #eef0f8 !important;
        border-right: 1px solid #e2e4f0;
    }
    
    [data-testid="stSidebar"] > div:first-child {
        background-color: #eef0f8 !important;
        background: #eef0f8 !important;
    }
    
    .main, .block-container {
        background-color: #f4f5fb !important;
        background: #f4f5fb !important;
    }
    
    section[data-testid="stAppViewContainer"] {
        background-color: #f4f5fb !important;
        background: #f4f5fb !important;
    }
    
    section[data-testid="stAppViewContainer"] > div {
        background-color: #f4f5fb !important;
        background: #f4f5fb !important;
    }
    
    /* Cards, charts, tables with light background on top of colored bg */
    .card, .kpi-card, [data-testid="stPlotlyChart"], .stDataFrame {
        background-color: #f8f9fa !important;
        border-radius: 16px;
        box-shadow: 0 8px 20px rgba(15, 23, 42, 0.06);
        padding: 1.25rem;
    }
    
    .block-container {
        max-width: 1300px;
        margin: auto;
        padding-top: 2rem;
        padding-bottom: 2rem;
    }
    
    /* Card hover effects */
    .card:hover {
        box-shadow: 0 10px 15px -3px rgba(0, 0, 0, 0.1), 0 4px 6px -2px rgba(0, 0, 0, 0.05);
        transform: scale(1.01);
    }
    
    .kpi-card {
        text-align: center;
        transition: all 0.2s ease;
    }
    
    .kpi-card:hover {
        box-shadow: 0 10px 15px -3px rgba(0, 0, 0, 0.1), 0 4px 6px -2px rgba(0, 0, 0, 0.05);
        transform: translateY(-4px) scale(1.01);
    }
    
    .kpi-value {
        font-size: 2.25rem;
        font-weight: 700;
        color: #1e293b;
        margin: 0.75rem 0;
        letter-spacing: -0.02em;
    }
    
    .kpi-label {
        font-size: 0.875rem;
        color: #64748b;
        text-transform: uppercase;
        letter-spacing: 0.1em;
        font-weight: 600;
    }
    
    [data-testid="stSidebar"] > div:first-child {
        padding-top: 1rem;
        padding-left: 0.75rem;
        padding-right: 0.75rem;
    }
    
    /* Reduce spacing in sidebar */
    [data-testid="stSidebar"] .stMarkdown {
        margin-bottom: 0.5rem;
    }
    
    [data-testid="stSidebar"] h1, [data-testid="stSidebar"] h2, [data-testid="stSidebar"] h3 {
        margin-top: 0.5rem;
        margin-bottom: 0.5rem;
    }
    
    /* Sidebar collapse handling - ensure it can always be reopened */
    [data-testid="stSidebar"] {
        min-width: 21rem !important;
    }
    
    /* When collapsed, keep a small visible area */
    [data-testid="stSidebar"][aria-expanded="false"] {
        min-width: 0 !important;
        width: 0 !important;
    }
    
    
    /* Typography Improvements */
    h1 {
        font-size: 2.75rem;
        font-weight: 800;
        line-height: 1.1;
        margin-bottom: 1rem;
        color: #0f172a;
        letter-spacing: -0.02em;
    }
    
    h2 {
        font-size: 1.875rem;
        font-weight: 700;
        line-height: 1.2;
        margin-bottom: 0.75rem;
        color: #1e293b;
    }
    
    h3 {
        font-size: 1.375rem;
        font-weight: 600;
        line-height: 1.3;
        color: #334155;
    }
    
    /* Subtitle styling */
    .subtitle {
        color: #64748b;
        font-size: 1rem;
        line-height: 1.6;
        font-weight: 400;
    }
    
    /* Hero/Header Section - Gradient Background */
    .hero-section {
        background: linear-gradient(135deg, #6366f1 0%, #8b5cf6 100%);
        border-radius: 20px;
        padding: 3rem 2.5rem;
        margin-bottom: 2.5rem;
        color: white;
        box-shadow: 0 10px 25px -5px rgba(99, 102, 241, 0.3), 0 8px 10px -6px rgba(99, 102, 241, 0.3);
    }
    
    .hero-badge {
        display: inline-block;
        background: rgba(255, 255, 255, 0.25);
        padding: 0.5rem 1.25rem;
        border-radius: 25px;
        font-size: 0.875rem;
        font-weight: 600;
        margin-bottom: 1.25rem;
        backdrop-filter: blur(10px);
        border: 1px solid rgba(255, 255, 255, 0.3);
    }
    
    .hero-title {
        font-size: 2.75rem;
        font-weight: 800;
        margin-bottom: 0.75rem;
        color: white;
        text-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
        letter-spacing: -0.02em;
    }
    
    .hero-subtitle {
        font-size: 1.125rem;
        opacity: 0.95;
        line-height: 1.7;
        font-weight: 400;
    }
    
    /* Navigation Bar - Light Card Style */
    .nav-button-group {
        display: flex;
        gap: 0.5rem;
        padding: 0.75rem;
        background: #f8f9fa;
        border-radius: 12px;
        box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.1);
        margin-bottom: 2rem;
        flex-wrap: wrap;
    }
    
    .nav-button {
        padding: 0.5rem 1rem;
        border-radius: 8px;
        border: none;
        background: transparent;
        color: #64748b;
        font-weight: 500;
        cursor: pointer;
        transition: all 0.2s ease;
    }
    
    .nav-button:hover {
        background: #f1f5f9;
        color: #1e293b;
        transform: scale(1.02);
    }
    
    .nav-button.active {
        background: #6366f1;
        color: white;
        font-weight: 600;
    }
    
    /* Sidebar toggle button in nav - always visible */
    #nav-sidebar-toggle {
        background: linear-gradient(135deg, #6366f1 0%, #8b5cf6 100%);
        color: white !important;
        font-weight: 600;
    }
    
    #nav-sidebar-toggle:hover {
        background: linear-gradient(135deg, #4f46e5 0%, #7c3aed 100%);
        color: white !important;
    }
    
    /* Radio Button Styling - Smooth Pill Design with Animations */
    .stRadio > div {
        display: flex;
        flex-direction: column;
        gap: 0.4rem;
    }
    
    /* Default state - all labels start unselected with entrance animation */
    .stRadio > div > label {
        padding: 0.75rem 1rem;
        border-radius: 12px;
        transition: all 0.25s cubic-bezier(0.4, 0, 0.2, 1) !important;
        cursor: pointer !important;
        background: #f8f9fa !important;
        border: 2px solid #e2e8f0 !important;
        margin-bottom: 0.4rem;
        font-weight: 500;
        color: #475569 !important;
        display: flex;
        align-items: center;
        position: relative;
        transform: translateX(0) scale(1) !important;
        box-shadow: 0 1px 3px rgba(0, 0, 0, 0.05) !important;
        opacity: 0;
        animation: slideInFromLeft 0.3s ease-out forwards;
        pointer-events: auto !important;
        user-select: none !important;
        -webkit-user-select: none !important;
    }
    
    /* Staggered entrance animation for each button */
    .stRadio > div > label:nth-child(1) { animation-delay: 0.1s; }
    .stRadio > div > label:nth-child(2) { animation-delay: 0.2s; }
    .stRadio > div > label:nth-child(3) { animation-delay: 0.3s; }
    .stRadio > div > label:nth-child(4) { animation-delay: 0.4s; }
    .stRadio > div > label:nth-child(5) { animation-delay: 0.5s; }
    
    /* Slide in from left animation */
    @keyframes slideInFromLeft {
        from {
            opacity: 0;
            transform: translateX(-20px) scale(0.95);
        }
        to {
            opacity: 1;
            transform: translateX(0) scale(1);
        }
    }
    
    /* Hover state for unselected buttons - smooth animation */
    .stRadio > div > label:hover:not(:has(> div[data-baseweb="radio"] > input:checked)) {
        background: #f1f5f9 !important;
        border-color: #6366f1 !important;
        transform: translateX(4px) scale(1.01) !important;
        box-shadow: 0 4px 8px rgba(99, 102, 241, 0.15) !important;
        color: #1e293b !important;
        transition: all 0.2s cubic-bezier(0.4, 0, 0.2, 1) !important;
    }
    
    /* Selected state - ONLY the checked one with smooth animation */
    .stRadio > div > label:has(> div[data-baseweb="radio"] > input[type="radio"]:checked) {
        background: linear-gradient(135deg, #6366f1 0%, #8b5cf6 100%) !important;
        color: white !important;
        font-weight: 600 !important;
        border-color: #6366f1 !important;
        box-shadow: 0 6px 12px rgba(99, 102, 241, 0.25), 0 0 0 2px rgba(99, 102, 241, 0.1) !important;
        transform: translateX(8px) scale(1.02) !important;
        transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1) !important;
    }
    
    
    /* Hover state for selected button */
    .stRadio > div > label:has(> div[data-baseweb="radio"] > input[type="radio"]:checked):hover {
        background: linear-gradient(135deg, #5b21b6 0%, #7c3aed 100%) !important;
        box-shadow: 0 8px 16px rgba(99, 102, 241, 0.35), 0 0 0 3px rgba(99, 102, 241, 0.15) !important;
        transform: translateX(10px) scale(1.03) !important;
        transition: all 0.2s cubic-bezier(0.4, 0, 0.2, 1) !important;
    }
    
    /* Ensure text color is white when selected */
    .stRadio > div > label:has(> div[data-baseweb="radio"] > input[type="radio"]:checked) > span {
        color: white !important;
        transition: color 0.2s ease !important;
    }
    
    /* Radio button circle styling with smooth animation */
    .stRadio > div > label > div[data-baseweb="radio"] {
        margin-right: 1rem;
        transition: all 0.25s cubic-bezier(0.4, 0, 0.2, 1) !important;
    }
    
    /* Animate radio circle when selected - smooth scale */
    .stRadio > div > label:has(> div[data-baseweb="radio"] > input[type="radio"]:checked) > div[data-baseweb="radio"] {
        transform: scale(1.15);
        transition: transform 0.25s cubic-bezier(0.4, 0, 0.2, 1) !important;
    }
    
    /* Smooth click feedback - minimal to prevent interference */
    .stRadio > div > label:active:not(:has(> div[data-baseweb="radio"] > input[type="radio"]:checked)) {
        transform: translateX(2px) scale(0.99) !important;
        transition: all 0.1s ease !important;
    }
    
    .stRadio > div > label:has(> div[data-baseweb="radio"] > input[type="radio"]:checked):active {
        transform: translateX(6px) scale(1.01) !important;
        transition: all 0.1s ease !important;
    }
    
    /* Ensure radio button input is clickable and not blocked */
    .stRadio > div > label > div[data-baseweb="radio"] > input[type="radio"] {
        pointer-events: auto !important;
        cursor: pointer !important;
    }
    
    /* Make entire label clickable */
    .stRadio > div > label {
        pointer-events: auto !important;
        cursor: pointer !important;
    }
    
    /* Ensure unselected buttons don't have selected styling */
    .stRadio > div > label:not(:has(> div[data-baseweb="radio"] > input[type="radio"]:checked)) {
        background: #f8f9fa !important;
        color: #475569 !important;
        border-color: #e2e8f0 !important;
        box-shadow: 0 1px 3px rgba(0, 0, 0, 0.05) !important;
        transform: translateX(0) scale(1) !important;
    }
    
    /* Ensure radio button input is clickable and not blocked */
    .stRadio > div > label > div[data-baseweb="radio"] > input[type="radio"] {
        pointer-events: auto !important;
        cursor: pointer !important;
        z-index: 10 !important;
    }
    
    /* Make entire label clickable */
    .stRadio > div > label {
        pointer-events: auto !important;
        cursor: pointer !important;
    }
    
    /* Tables and DataFrames - Light Card Style */
    .dataframe {
        background: #f8f9fa;
        border-radius: 12px;
        box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.1);
    }
    
    /* Expander styling */
    .streamlit-expanderHeader {
        background: #f8f9fa;
        border-radius: 8px;
        transition: all 0.2s ease;
    }
    
    .streamlit-expanderHeader:hover {
        background: #f1f3f5;
    }
    
    /* Metric cards */
    [data-testid="stMetricValue"] {
        font-size: 2rem;
        font-weight: 700;
    }
    
    /* Smooth transitions for all interactive elements */
    button, .card, .kpi-card {
        transition: all 0.2s ease;
    }
    
    button:hover {
        transform: scale(1.02);
    }

    
    /* Responsive */
    @media (max-width: 768px) {
        .block-container {
            padding: 1rem;
        }
        
        .hero-title {
            font-size: 1.75rem;
        }
        
        .nav-button-group {
            flex-direction: column;
        }
    }
    
    /* Smooth Transitions */
    button, .card, .kpi-card, .stButton > button {
    transition: background-color 0.2s ease, box-shadow 0.2s ease, transform 0.2s ease;
    }
</style>
""", unsafe_allow_html=True)

# Initialize session state for page navigation
if 'current_page' not in st.session_state:
    st.session_state.current_page = "Overview"

# Navigation Bar (already styled in main CSS)

nav_col1, nav_col2, nav_col3, nav_col4, nav_col5, nav_col6, nav_col7, nav_col8 = st.columns([2, 1, 1.5, 1.5, 1.5, 1, 1, 1])

with nav_col1:
    st.markdown('<div style="font-size: 24px; font-weight: bold; color: #1DB954;">🎵 Tune Dashboard</div>', unsafe_allow_html=True)

with nav_col2:
    is_home_active = st.session_state.current_page == "Overview"
    home_style = "color: #FF4444; border-bottom: 2px solid #FF4444;" if is_home_active else "color: #333;"
    if st.button("Home", key="btn_home", use_container_width=True, type="primary" if is_home_active else "secondary"):
        st.session_state.current_page = "Overview"
        st.rerun()

with nav_col3:
    is_reports_active = st.session_state.current_page in ["Charts", "Analysis", "Artist", "Album"]
    
    # Map current page to dropdown index
    report_options = ["Reports", "Charts", "Artist", "Album", "Analysis"]
    current_report_index = 0
    if st.session_state.current_page == "Charts":
        current_report_index = 1
    elif st.session_state.current_page == "Artist":
        current_report_index = 2
    elif st.session_state.current_page == "Album":
        current_report_index = 3
    elif st.session_state.current_page == "Analysis":
        current_report_index = 4
    
    selected_report = st.selectbox(
        "",
        report_options,
        index=current_report_index,
        key="reports_select",
        label_visibility="collapsed"
    )
    
    if selected_report != "Reports" and selected_report != st.session_state.current_page:
        if selected_report == "Charts":
            st.session_state.current_page = "Charts"
        elif selected_report == "Artist":
            st.session_state.current_page = "Artist"
        elif selected_report == "Album":
            st.session_state.current_page = "Album"
        elif selected_report == "Analysis":
            st.session_state.current_page = "Analysis"
        st.rerun()

with nav_col4:
    st.button("Repertoire", key="btn_repertoire", use_container_width=True, disabled=True)

with nav_col5:
    st.button("New Songs Release", key="btn_songs", use_container_width=True, disabled=True)

with nav_col6:
    st.button("Resource", key="btn_resource", use_container_width=True, disabled=True)

with nav_col7:
    st.button("Contact", key="btn_contact", use_container_width=True, disabled=True)

with nav_col8:
    st.button("Account ▼", key="btn_account", use_container_width=True, disabled=True)


@st.cache_data
def load_csv(file_name: str):
    try:
        df = pd.read_csv(file_name)
        return df, None
    except FileNotFoundError:
        return None, f"File not found: {file_name}"
    except Exception as e:
        return None, f"Error loading {file_name}: {e}"


# Load CSVs once at the top
jio_df, jio_err = load_csv("data/jiosaavn-report.csv")
wynk_df, wynk_err = load_csv("data/wynk-report.csv")

# Create combined DataFrame for charts
if jio_df is not None and wynk_df is not None:
    # Add Platform column to each DataFrame
    jio_df_copy = jio_df.copy()
    jio_df_copy['Platform'] = 'JioSaavn'
    
    wynk_df_copy = wynk_df.copy()
    wynk_df_copy['Platform'] = 'Wynk'
    
    # Concatenate the DataFrames
    combined_df = pd.concat([jio_df_copy, wynk_df_copy], ignore_index=True)
else:
    combined_df = None


# Sidebar menu (can be toggled)
with st.sidebar:
    st.markdown('<div style="font-size: 1.5rem; font-weight: bold; margin-bottom: 1rem;">📊 Dashboard</div>', unsafe_allow_html=True)
    st.markdown("---")
    # Sync with session state
    page = st.radio(
        "Select a section:",
        ["Overview", "Charts", "Analysis", "Artist", "Album"],
        index=["Overview", "Charts", "Analysis", "Artist", "Album"].index(st.session_state.current_page) if st.session_state.current_page in ["Overview", "Charts", "Analysis", "Artist", "Album"] else 0,
        label_visibility="visible",
        key="sidebar_radio"
    )
    # Update session state when sidebar changes and rerun immediately
    if page != st.session_state.current_page:
        st.session_state.current_page = page
        st.rerun()



# Display content based on selected page (use session state)
current_page = st.session_state.current_page

if current_page == "Overview":
    # Hero Section
    st.markdown("""
    <div class="hero-section">
        <div class="hero-badge">🎵 Tune Dashboard</div>
        <div class="hero-title">Tune Dashboard – JioSaavn & Wynk</div>
        <div class="hero-subtitle">Comprehensive analytics and insights for music streaming performance across JioSaavn and Wynk platforms</div>
    </div>
    """, unsafe_allow_html=True)
    
    # KPI Cards
    if jio_df is not None and wynk_df is not None:
        # Calculate KPIs
        total_rows = len(jio_df) + len(wynk_df)
        unique_tracks_jio = jio_df['song_name'].nunique() if 'song_name' in jio_df.columns else 0
        unique_tracks_wynk = wynk_df['song_name'].nunique() if 'song_name' in wynk_df.columns else 0
        unique_tracks = unique_tracks_jio + unique_tracks_wynk
        
        # Standardize artist columns for unique count
        if 'artist_name' in jio_df.columns:
            unique_artists_jio = jio_df['artist_name'].nunique()
        else:
            unique_artists_jio = 0
        if 'artist' in wynk_df.columns:
            unique_artists_wynk = wynk_df['artist'].nunique()
        else:
            unique_artists_wynk = 0
        unique_artists = unique_artists_jio + unique_artists_wynk
        
        # Calculate total revenue if available
        try:
            jio_df['income'] = pd.to_numeric(jio_df.get('income', 0), errors='coerce').fillna(0)
            wynk_df['income'] = pd.to_numeric(wynk_df.get('income', 0), errors='coerce').fillna(0)
            total_revenue = jio_df['income'].sum() + wynk_df['income'].sum()
        except:
            total_revenue = 0
    
    kpi_col1, kpi_col2, kpi_col3, kpi_col4 = st.columns(4)
    
    with kpi_col1:
        st.markdown(f"""
        <div class="kpi-card">
            <div class="kpi-label">Total Records</div>
            <div class="kpi-value">{total_rows:,}</div>
        </div>
        """, unsafe_allow_html=True)
    
    with kpi_col2:
        st.markdown(f"""
        <div class="kpi-card">
            <div class="kpi-label">Unique Tracks</div>
            <div class="kpi-value">{unique_tracks:,}</div>
        </div>
        """, unsafe_allow_html=True)
    
    with kpi_col3:
        st.markdown(f"""
        <div class="kpi-card">
            <div class="kpi-label">Unique Artists</div>
            <div class="kpi-value">{unique_artists:,}</div>
        </div>
        """, unsafe_allow_html=True)
    
    with kpi_col4:
        st.markdown(f"""
        <div class="kpi-card">
            <div class="kpi-label">Total Revenue</div>
            <div class="kpi-value">${total_revenue:,.2f}</div>
        </div>
        """, unsafe_allow_html=True)
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    # Platform Cards
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown('<div class="card">', unsafe_allow_html=True)
        st.markdown("### 🎧 JioSaavn Report")
        st.markdown("**Streaming Performance Summary**")
        if jio_err:
            st.error(jio_err)
        else:
            st.markdown(f'<div style="font-size: 2rem; font-weight: bold; color: #1DB954; margin: 1rem 0;">{len(jio_df):,} rows</div>', unsafe_allow_html=True)
            with st.expander("View raw data"):
                st.dataframe(jio_df)
        st.markdown('</div>', unsafe_allow_html=True)
    
    with col2:
        st.markdown('<div class="card">', unsafe_allow_html=True)
        st.markdown("### 🎼 Wynk Report")
        st.markdown("**Streaming Performance Summary**")
        if wynk_err:
            st.error(wynk_err)
        else:
            st.markdown(f'<div style="font-size: 2rem; font-weight: bold; color: #FF6B6B; margin: 1rem 0;">{len(wynk_df):,} rows</div>', unsafe_allow_html=True)
            with st.expander("View raw data"):
                st.dataframe(wynk_df)
        st.markdown('</div>', unsafe_allow_html=True)

elif current_page == "Charts":
    st.header("Interactive Charts")
    
    if jio_err or wynk_err:
        st.error("Cannot display charts: Data files not loaded properly.")
        if jio_err:
            st.error(f"JioSaavn: {jio_err}")
        if wynk_err:
            st.error(f"Wynk: {wynk_err}")
    elif combined_df is not None:
        try:
            # Convert income and total to numeric (they might be strings)
            # Using column 'income' as revenue
            if 'income' in combined_df.columns:
                combined_df['income'] = pd.to_numeric(combined_df['income'], errors='coerce')
            else:
                st.error("Column 'income' not found in the dataset.")
                st.stop()
            
            # Using column 'total' as total streams
            if 'total' in combined_df.columns:
                combined_df['total'] = pd.to_numeric(combined_df['total'], errors='coerce')
            else:
                st.error("Column 'total' not found in the dataset.")
                st.stop()
            
            # 1. DSP Reports - Revenue vs Store Name (Platform)
            st.markdown('<div class="card">', unsafe_allow_html=True)
            st.subheader("DSP Reports")
            st.markdown("**Revenue vs Store Name**")
            if 'Platform' in combined_df.columns:
                platform_revenue = combined_df.groupby('Platform')['income'].sum().reset_index()
                platform_revenue = platform_revenue.sort_values('income', ascending=False)
                fig_dsp = px.bar(
                    platform_revenue,
                    x='Platform',
                    y='income',
                    title='Revenue vs Store Name',
                    labels={'income': 'Revenue', 'Platform': 'Store Name'},
                    color='Platform',
                    color_discrete_map={'JioSaavn': '#1DB954', 'Wynk': '#FF6B6B'}
                )
                fig_dsp.update_layout(
                    showlegend=False,
                    xaxis_title="Store Name",
                    yaxis_title="Revenue",
                    height=400
                )
                st.plotly_chart(fig_dsp, use_container_width=True)
            st.markdown('</div>', unsafe_allow_html=True)
            
            # 2. Streaming Trend - Pie Chart
            st.markdown('<div class="card">', unsafe_allow_html=True)
            st.subheader("Streaming Trend")
            st.markdown("**Quantity and Revenue**")
            
            # Calculate streaming breakdown for JioSaavn
            if jio_df is not None:
                jio_df['ad_supported_streams'] = pd.to_numeric(jio_df.get('ad_supported_streams', 0), errors='coerce').fillna(0)
                jio_df['subscription_streams'] = pd.to_numeric(jio_df.get('subscription_streams', 0), errors='coerce').fillna(0)
                jio_df['jio_trial_streams'] = pd.to_numeric(jio_df.get('jio_trial_streams', 0), errors='coerce').fillna(0)
                
                streaming_data = {
                    'Ad Supported Audio': jio_df['ad_supported_streams'].sum(),
                    'Subscription Streams': jio_df['subscription_streams'].sum(),
                    'Jio Trial Streams': jio_df['jio_trial_streams'].sum(),
                }
                
                # Calculate total and percentages
                total_streams = sum(streaming_data.values())
                if total_streams > 0:
                    streaming_df = pd.DataFrame({
                        'Streaming Type': list(streaming_data.keys()),
                        'Quantity': list(streaming_data.values()),
                        'Percentage': [v/total_streams*100 for v in streaming_data.values()]
                    })
                    streaming_df = streaming_df[streaming_df['Quantity'] > 0]  # Remove zero values
                    
                    fig_pie = px.pie(
                        streaming_df,
                        values='Quantity',
                        names='Streaming Type',
                        title='Streaming Trend - Quantity Distribution',
                        color_discrete_sequence=px.colors.qualitative.Set3
                    )
                    fig_pie.update_traces(textposition='inside', textinfo='percent+label')
                    fig_pie.update_layout(height=500)
                    st.plotly_chart(fig_pie, use_container_width=True)
            st.markdown('</div>', unsafe_allow_html=True)
            
            # 3. Language-wise Revenue Trend
            st.markdown('<div class="card">', unsafe_allow_html=True)
            st.subheader("Language-wise Revenue Trend")
            st.markdown("**Revenue vs Language**")
            if 'language' in combined_df.columns:
                lang_revenue = combined_df.groupby('language')['income'].sum().reset_index()
                lang_revenue = lang_revenue.sort_values('income', ascending=False).head(10)
                fig_lang = px.bar(
                    lang_revenue,
                    x='language',
                    y='income',
                    title='Revenue vs Language',
                    labels={'income': 'Revenue', 'language': 'Language'},
                    color='income',
                    color_continuous_scale='Blues'
                )
                fig_lang.update_layout(
                    xaxis_title="Language",
                    yaxis_title="Revenue",
                    height=400,
                    showlegend=False
                )
                st.plotly_chart(fig_lang, use_container_width=True)
            st.markdown('</div>', unsafe_allow_html=True)
            
            # 4. Label-wise Revenue (Top Labels)
            st.markdown('<div class="card">', unsafe_allow_html=True)
            st.subheader("Label-wise Revenue")
            st.markdown("**Revenue vs Label**")
            if 'label' in combined_df.columns:
                label_revenue = combined_df.groupby('label')['income'].sum().reset_index()
                label_revenue = label_revenue.sort_values('income', ascending=False).head(15)
                fig_label = px.bar(
                    label_revenue,
                    x='label',
                    y='income',
                    title='Revenue vs Label (Top 15)',
                    labels={'income': 'Revenue', 'label': 'Label'},
                    color='income',
                    color_continuous_scale='Greens'
                )
                fig_label.update_layout(
                    xaxis_title="Label",
                    yaxis_title="Revenue",
                    height=500,
                    xaxis={'tickangle': -45},
                    showlegend=False
                )
                st.plotly_chart(fig_label, use_container_width=True)
            st.markdown('</div>', unsafe_allow_html=True)
            
            # 5. Platform Comparison - Stacked Bar Chart (Revenue breakdown)
            st.markdown('<div class="card">', unsafe_allow_html=True)
            st.subheader("Platform Revenue Breakdown")
            st.markdown("**JioSaavn vs Wynk Revenue Comparison**")
            if 'Platform' in combined_df.columns:
                # Create stacked data
                jio_total = combined_df[combined_df['Platform'] == 'JioSaavn']['income'].sum()
                wynk_total = combined_df[combined_df['Platform'] == 'Wynk']['income'].sum()
                
                stacked_data = pd.DataFrame({
                    'Platform': ['JioSaavn', 'Wynk'],
                    'Revenue': [jio_total, wynk_total]
                })
                
                fig_stacked = px.bar(
                    stacked_data,
                    x='Platform',
                    y='Revenue',
                    title='Platform Revenue Comparison',
                    labels={'Revenue': 'Revenue', 'Platform': 'Platform'},
                    color='Platform',
                    color_discrete_map={'JioSaavn': '#1DB954', 'Wynk': '#FF6B6B'}
                )
                fig_stacked.update_layout(
                    xaxis_title="Platform",
                    yaxis_title="Revenue",
                    height=400,
                    showlegend=False
                )
                st.plotly_chart(fig_stacked, use_container_width=True)
            st.markdown('</div>', unsafe_allow_html=True)
        except Exception as e:
            st.error(f"Error generating charts: {str(e)}")
        
    else:
        st.warning("Data not available for charts.")

elif current_page == "Analysis":
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.header("Analysis & Project Report Text")
    st.markdown('</div>', unsafe_allow_html=True)
    
    # NOTE: The analysis text below can be directly used in my academic project report.
    
    if jio_err or wynk_err:
        st.error("Cannot generate analysis: Data files not loaded properly.")
        if jio_err:
            st.error(f"JioSaavn: {jio_err}")
        if wynk_err:
            st.error(f"Wynk: {wynk_err}")
    elif combined_df is not None:
        try:
            # Convert income and total to numeric (they might be strings)
            # Using column 'income' as revenue
            if 'income' not in combined_df.columns:
                st.error("Column 'income' not found in the dataset. Cannot perform analysis.")
                st.stop()
            combined_df['income'] = pd.to_numeric(combined_df['income'], errors='coerce')
            
            # Using column 'total' as total streams
            if 'total' not in combined_df.columns:
                st.error("Column 'total' not found in the dataset. Cannot perform analysis.")
                st.stop()
            combined_df['total'] = pd.to_numeric(combined_df['total'], errors='coerce')
            
            # Check for Platform column
            if 'Platform' not in combined_df.columns:
                st.error("Platform column not found. Cannot perform platform analysis.")
                st.stop()
            
            # Calculate totals by platform
            jio_total_revenue = combined_df[combined_df['Platform'] == 'JioSaavn']['income'].sum()
            wynk_total_revenue = combined_df[combined_df['Platform'] == 'Wynk']['income'].sum()
            overall_total_revenue = jio_total_revenue + wynk_total_revenue
            
            jio_total_streams = combined_df[combined_df['Platform'] == 'JioSaavn']['total'].sum()
            wynk_total_streams = combined_df[combined_df['Platform'] == 'Wynk']['total'].sum()
            overall_total_streams = jio_total_streams + wynk_total_streams
            
            # Calculate percentage contributions
            jio_revenue_pct = (jio_total_revenue / overall_total_revenue * 100) if overall_total_revenue > 0 else 0
            wynk_revenue_pct = (wynk_total_revenue / overall_total_revenue * 100) if overall_total_revenue > 0 else 0
            
            jio_streams_pct = (jio_total_streams / overall_total_streams * 100) if overall_total_streams > 0 else 0
            wynk_streams_pct = (wynk_total_streams / overall_total_streams * 100) if overall_total_streams > 0 else 0
            
            # Standardize artist column names for analysis
            if 'artist_name' in combined_df.columns or 'artist' in combined_df.columns:
                combined_df['artist_standardized'] = combined_df.apply(
                    lambda row: row.get('artist_name', 'Unknown') if row['Platform'] == 'JioSaavn' else row.get('artist', 'Unknown'),
                    axis=1
                )
            else:
                st.warning("Artist columns not found. Using placeholder for artist analysis.")
                combined_df['artist_standardized'] = 'Unknown'
            
            # Top 5 tracks by revenue (income)
            if 'song_name' in combined_df.columns:
                top_tracks = combined_df.nlargest(5, 'income')[['song_name', 'Platform', 'income', 'total']].copy()
            else:
                st.warning("Song name column not found. Cannot generate top tracks.")
                top_tracks = pd.DataFrame()
            
            # Top 5 artists by revenue (income)
            if 'artist_standardized' in combined_df.columns:
                artist_revenue = combined_df.groupby('artist_standardized')['income'].sum().reset_index()
                artist_revenue = artist_revenue.sort_values('income', ascending=False).head(5)
            else:
                artist_revenue = pd.DataFrame()
        except Exception as e:
            st.error(f"Error processing data for analysis: {str(e)}")
            st.stop()
        
        # Function to generate report text
        def generate_report_text():
            report = []
            report.append("=" * 70)
            report.append("MUSIC STREAMING PLATFORM ANALYSIS REPORT")
            report.append("=" * 70)
            report.append("")
            
            # Short intro about the dataset
            report.append("1. DATASET OVERVIEW")
            report.append("-" * 70)
            report.append(f"This analysis is based on streaming data from two major music platforms: JioSaavn and Wynk.")
            report.append(f"The dataset contains {len(combined_df):,} total records, with {len(jio_df):,} records from JioSaavn")
            report.append(f"and {len(wynk_df):,} records from Wynk. The data includes song information, streaming metrics,")
            report.append("revenue figures, and artist details.")
            report.append("")
            
            # Comparison: JioSaavn vs Wynk
            report.append("2. PLATFORM COMPARISON: JioSaavn vs Wynk")
            report.append("-" * 70)
            report.append(f"Total Revenue Analysis:")
            report.append(f"  • JioSaavn: ${jio_total_revenue:,.2f} ({jio_revenue_pct:.2f}% of total revenue)")
            report.append(f"  • Wynk: ${wynk_total_revenue:,.2f} ({wynk_revenue_pct:.2f}% of total revenue)")
            report.append(f"  • Overall Total: ${overall_total_revenue:,.2f}")
            report.append("")
            report.append(f"Total Streams Analysis:")
            report.append(f"  • JioSaavn: {jio_total_streams:,.0f} streams ({jio_streams_pct:.2f}% of total streams)")
            report.append(f"  • Wynk: {wynk_total_streams:,.0f} streams ({wynk_streams_pct:.2f}% of total streams)")
            report.append(f"  • Overall Total: {overall_total_streams:,.0f} streams")
            report.append("")
            
            if jio_revenue_pct > wynk_revenue_pct:
                report.append(f"JioSaavn leads in revenue generation, contributing {jio_revenue_pct:.2f}% of the total revenue,")
                report.append(f"while Wynk accounts for {wynk_revenue_pct:.2f}% of the total revenue.")
            else:
                report.append(f"Wynk leads in revenue generation, contributing {wynk_revenue_pct:.2f}% of the total revenue,")
                report.append(f"while JioSaavn accounts for {jio_revenue_pct:.2f}% of the total revenue.")
            report.append("")
            
            # Comment on best month/period (if date column exists)
            report.append("3. TEMPORAL ANALYSIS")
            report.append("-" * 70)
            report.append("Note: The dataset does not contain date or month information, therefore temporal")
            report.append("analysis (best performing months/periods) cannot be performed. If date information")
            report.append("were available, this section would highlight the top 3 months or time periods by")
            report.append("revenue and streaming metrics.")
            report.append("")
            
            # Top tracks/artists
            report.append("4. TOP PERFORMING TRACKS")
            report.append("-" * 70)
            if not top_tracks.empty and 'song_name' in top_tracks.columns:
                report.append("Top 5 tracks by revenue:")
                for idx, (_, track) in enumerate(top_tracks.iterrows(), 1):
                    report.append(f"  {idx}. {track['song_name']} ({track['Platform']}) - Revenue: ${track['income']:,.2f}, Streams: {track['total']:,.0f}")
            else:
                report.append("Top tracks data not available.")
            report.append("")
            
            report.append("5. TOP PERFORMING ARTISTS")
            report.append("-" * 70)
            if not artist_revenue.empty and 'artist_standardized' in artist_revenue.columns:
                report.append("Top 5 artists by total revenue:")
                for idx, (_, artist) in enumerate(artist_revenue.iterrows(), 1):
                    report.append(f"  {idx}. {artist['artist_standardized']} - Total Revenue: ${artist['income']:,.2f}")
            else:
                report.append("Top artists data not available.")
            report.append("")
            
            # Conclusion
            report.append("6. CONCLUSION")
            report.append("-" * 70)
            if jio_revenue_pct > wynk_revenue_pct:
                report.append(f"This analysis reveals that JioSaavn is the dominant platform in terms of revenue generation,")
                report.append(f"accounting for {jio_revenue_pct:.2f}% of total revenue compared to Wynk's {wynk_revenue_pct:.2f}%.")
            else:
                report.append(f"This analysis reveals that Wynk is the dominant platform in terms of revenue generation,")
                report.append(f"accounting for {wynk_revenue_pct:.2f}% of total revenue compared to JioSaavn's {jio_revenue_pct:.2f}%.")
            report.append(f"The combined platforms generated a total revenue of ${overall_total_revenue:,.2f} from")
            report.append(f"{overall_total_streams:,.0f} total streams, indicating significant engagement and monetization")
            report.append("potential in the Indian music streaming market.")
            report.append("")
            report.append("=" * 70)
            
            return "\n".join(report)
        
        # Generate the report
        report_text = generate_report_text()
        
        # Display key metrics
        st.subheader("Key Metrics")
        col1, col2, col3, col4 = st.columns(4)
        
        with col1:
            st.metric("JioSaavn Revenue", f"${jio_total_revenue:,.2f}", f"{jio_revenue_pct:.2f}%")
        
        with col2:
            st.metric("Wynk Revenue", f"${wynk_total_revenue:,.2f}", f"{wynk_revenue_pct:.2f}%")
        
        with col3:
            st.metric("JioSaavn Streams", f"{jio_total_streams:,.0f}", f"{jio_streams_pct:.2f}%")
        
        with col4:
            st.metric("Wynk Streams", f"{wynk_total_streams:,.0f}", f"{wynk_streams_pct:.2f}%")
        
        # Display the full report
        st.subheader("Full Analysis Report")
        st.text_area(
            "Report Text",
            value=report_text,
            height=500,
            help="This report can be directly used in your academic project report."
        )
        
        # Download button
        st.download_button(
            label="📥 Download Report as .txt",
            data=report_text,
            file_name="music_streaming_analysis_report.txt",
            mime="text/plain",
            help="Download the analysis report as a text file for your project."
        )
        
    else:
        st.warning("Data not available for analysis.")

elif current_page == "Artist":
    st.markdown("""
    <style>
    .artist-header {
        font-size: 36px;
        font-weight: bold;
        color: #333;
        text-align: center;
        margin-bottom: 10px;
    }
    .artist-divider {
        border-top: 2px solid #333;
        margin: 10px auto 20px;
        width: 100px;
    }
    </style>
    """, unsafe_allow_html=True)
    
    st.markdown('<div class="artist-header">Artist</div>', unsafe_allow_html=True)
    st.markdown('<div class="artist-divider"></div>', unsafe_allow_html=True)
    
    if jio_err or wynk_err:
        st.error("Cannot display artist data: Data files not loaded properly.")
    elif combined_df is not None:
        try:
            # Prepare artist data
            if 'income' in combined_df.columns:
                combined_df['income'] = pd.to_numeric(combined_df['income'], errors='coerce')
            if 'total' in combined_df.columns:
                combined_df['total'] = pd.to_numeric(combined_df['total'], errors='coerce')
            
            # Standardize artist column
            if 'artist_name' in combined_df.columns or 'artist' in combined_df.columns:
                combined_df['artist_standardized'] = combined_df.apply(
                    lambda row: row.get('artist_name', 'Unknown') if row.get('Platform') == 'JioSaavn' else row.get('artist', 'Unknown'),
                    axis=1
                )
            else:
                st.error("Artist columns not found.")
                st.stop()
            
            # Group by artist and calculate totals
            artist_data = combined_df.groupby('artist_standardized').agg({
                'income': 'sum',
                'total': 'sum'
            }).reset_index()
            artist_data.columns = ['Artist', 'Revenue', 'Total']
            artist_data = artist_data.sort_values('Revenue', ascending=False)
            
            # Search and pagination controls
            col1, col2 = st.columns([1, 3])
            with col1:
                entries_per_page = st.selectbox("Entries per page", [10, 13, 25, 50, 100], index=1)
            with col2:
                search_query = st.text_input("Search:", placeholder="Search by artist name...")
            
            # Filter by search
            if search_query:
                artist_data = artist_data[artist_data['Artist'].str.contains(search_query, case=False, na=False)]
            
            # Pagination
            total_entries = len(artist_data)
            total_pages = (total_entries - 1) // entries_per_page + 1 if total_entries > 0 else 1
            
            page_num = st.number_input("Page", min_value=1, max_value=total_pages, value=1, step=1, key="artist_page")
            start_idx = (page_num - 1) * entries_per_page
            end_idx = start_idx + entries_per_page
            
            # Display data
            display_data = artist_data.iloc[start_idx:end_idx].copy()
            display_data['Revenue'] = display_data['Revenue'].round(3)
            display_data['Total'] = display_data['Total'].round(3)
            
            st.dataframe(
                display_data,
                use_container_width=True,
                hide_index=True,
                column_config={
                    "Artist": st.column_config.TextColumn("Artist", width="large"),
                    "Revenue": st.column_config.NumberColumn("Revenue", format="%.3f"),
                    "Total": st.column_config.NumberColumn("Total", format="%.3f")
                }
            )
            
            st.caption(f"Showing {start_idx + 1} to {min(end_idx, total_entries)} of {total_entries} entries")
            
        except Exception as e:
            st.error(f"Error processing artist data: {str(e)}")
    else:
        st.warning("Data not available for artist analysis.")

elif current_page == "Album":
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.markdown('<h1 style="text-align: center; margin-bottom: 1rem;">Album</h1>', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)
    
    if jio_err or wynk_err:
        st.error("Cannot display album data: Data files not loaded properly.")
    elif combined_df is not None:
        try:
            # Prepare album data
            if 'income' in combined_df.columns:
                combined_df['income'] = pd.to_numeric(combined_df['income'], errors='coerce')
            if 'total' in combined_df.columns:
                combined_df['total'] = pd.to_numeric(combined_df['total'], errors='coerce')
            
            # Standardize artist and album columns
            if 'artist_name' in combined_df.columns or 'artist' in combined_df.columns:
                combined_df['artist_standardized'] = combined_df.apply(
                    lambda row: row.get('artist_name', 'Unknown') if row.get('Platform') == 'JioSaavn' else row.get('artist', 'Unknown'),
                    axis=1
                )
            else:
                combined_df['artist_standardized'] = 'Unknown'
            
            # Group by album and calculate totals
            album_data = combined_df.groupby(['album_name', 'artist_standardized']).agg({
                'income': 'sum',
                'total': 'sum',
                'isrc': 'first'  # Get first ISRC as project code
            }).reset_index()
            
            # Create project code from ISRC (first part)
            album_data['Project Code'] = album_data['isrc'].astype(str).str[:8].str.upper()
            album_data = album_data.rename(columns={
                'album_name': 'Release',
                'artist_standardized': 'Artist',
                'income': 'Revenue',
                'total': 'Total'
            })
            
            # Select and reorder columns
            album_data = album_data[['Release', 'Artist', 'Project Code', 'Revenue', 'Total']]
            album_data = album_data.sort_values('Revenue', ascending=False)
            
            # Search and pagination controls
            col1, col2 = st.columns([1, 3])
            with col1:
                entries_per_page = st.selectbox("Entries per page", [10, 13, 25, 50, 100], index=0)
            with col2:
                search_query = st.text_input("Search:", placeholder="Search by release, artist, or project code...", key="album_search")
            
            # Filter by search
            if search_query:
                mask = (
                    album_data['Release'].str.contains(search_query, case=False, na=False) |
                    album_data['Artist'].str.contains(search_query, case=False, na=False) |
                    album_data['Project Code'].str.contains(search_query, case=False, na=False)
                )
                album_data = album_data[mask]
            
            # Pagination
            total_entries = len(album_data)
            total_pages = (total_entries - 1) // entries_per_page + 1 if total_entries > 0 else 1
            
            page_num = st.number_input("Page", min_value=1, max_value=total_pages, value=1, step=1, key="album_page")
            start_idx = (page_num - 1) * entries_per_page
            end_idx = start_idx + entries_per_page
            
            # Display data
            display_data = album_data.iloc[start_idx:end_idx].copy()
            display_data['Revenue'] = display_data['Revenue'].round(3)
            display_data['Total'] = display_data['Total'].round(3)
            
            st.dataframe(
                display_data,
                use_container_width=True,
                hide_index=True,
                column_config={
                    "Release": st.column_config.TextColumn("Release", width="large"),
                    "Artist": st.column_config.TextColumn("Artist", width="medium"),
                    "Project Code": st.column_config.TextColumn("Project Code", width="small"),
                    "Revenue": st.column_config.NumberColumn("Revenue", format="%.3f"),
                    "Total": st.column_config.NumberColumn("Total", format="%.3f")
                }
            )
            
            st.caption(f"Showing {start_idx + 1} to {min(end_idx, total_entries)} of {total_entries} entries")
            
        except Exception as e:
            st.error(f"Error processing album data: {str(e)}")
            import traceback
            st.error(traceback.format_exc())
    else:
        st.warning("Data not available for album analysis.")
    