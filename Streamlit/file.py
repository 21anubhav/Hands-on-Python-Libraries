import streamlit as st
import pandas as pd


st.set_page_config(page_title="Dashboard For Multiple Uploads", layout="wide")

# Background color
def set_bg_color():
    st.markdown(
        """
        <style>
        .stApp {
            background: linear-gradient(135deg, #4facfe, #6a11cb, #f953c6);
            color: #ffffff;
        }
        h1, h2, h3, h4 {
            color: #ffeb3b;  /* Bright yellow for headings */
        }
        .css-1d391kg p {
            color: #f1f1f1;  /* Light gray for normal text */
        }
        </style>
        """,
        unsafe_allow_html=True
    )

set_bg_color()

st.markdown("<h1 style='text-align: center;'>🌟 Welcome to Our Dashboard 🌟</h1>", unsafe_allow_html=True)
st.markdown("<h3 style='text-align: center;'>Upload, Explore & Visualize Your Data with Ease 🚀</h3>", unsafe_allow_html=True)

# Sidebar
st.sidebar.title("📂 Navigation")
menu = st.sidebar.radio("Choose a section:", ["Home", "CSV/Excel", "Image", "Video", "Audio"])

if menu == "Home":
    st.subheader("✨ Features of this Dashboard")
    st.markdown("""
    - 📊 Upload **CSV/Excel** and analyze instantly  
    - 📸 View uploaded **images**  
    - 🎥 Play uploaded **videos**  
    - 🎵 Play uploaded **audio files**  
    - 📈 Automatic data **visualization**
    """)
    st.success("👉 Use the sidebar to start uploading your files!")

elif menu == "CSV/Excel":
    st.subheader("📊 Upload and Explore CSV/Excel File")
    file = st.file_uploader("Upload CSV or Excel file:", type=['csv', 'xlsx'])

    if file is not None:
        try:
            if file.name.endswith('.csv'):
                df = pd.read_csv(file)
            else:
                df = pd.read_excel(file)

            st.success(f"✅ File `{file.name}` uploaded successfully!")

            # Preview
            st.write("### 🔍 Data Preview:")
            st.dataframe(df.head())

            st.write(f"**Rows:** {df.shape[0]}, **Columns:** {df.shape[1]}")
            st.write("**Columns:**", list(df.columns))

            # Summary
            st.write("### 📊 Summary Statistics")
            st.write(df.describe())

            # Download processed CSV
            csv = df.to_csv(index=False).encode('utf-8')
            st.download_button("⬇️ Download Processed CSV", csv, "processed.csv", "text/csv")

            # Visualization Options
            st.write("### 📈 Choose a Visualization")
            chart_type = st.selectbox("Select Chart Type:", ["Line", "Bar", "Area", "Pie"])

            if chart_type in ["Line", "Bar", "Area"]:
                col = st.selectbox("Choose column for visualization:", df.columns)
                if chart_type == "Line":
                    st.line_chart(df[col])
                elif chart_type == "Bar":
                    st.bar_chart(df[col])
                elif chart_type == "Area":
                    st.area_chart(df[col])

            elif chart_type == "Pie":
                col = st.selectbox("Choose column for Pie Chart:", df.columns)
                pie_data = df[col].value_counts()
                st.write("Pie Chart Distribution")
                st.write(pie_data.plot.pie(autopct="%1.1f%%").get_figure())
                st.pyplot()

        except Exception as e:
            st.error(f"❌ Error loading file: {e}")

elif menu == "Image":
    st.subheader("🖼️ Upload and Display Image")
    img_file = st.file_uploader("Upload Image:", type=['png', 'jpg', 'jpeg'])
    if img_file is not None:
        st.image(img_file, caption="Uploaded Image", use_column_width=True)

elif menu == "Video":
    st.subheader("🎥 Upload and Play Video")
    video_file = st.file_uploader("Upload Video:", type=['mp4', 'mkv'])
    if video_file is not None:
        st.video(video_file, start_time=0)

elif menu == "Audio":
    st.subheader("🎵 Upload and Play Audio")
    audio_file = st.file_uploader("Upload Audio:", type=['mp3', 'wav'])
    if audio_file is not None:
        st.audio(audio_file, format="audio/mp3")
