import streamlit as st
from report_pdf import generate_pdf_report

if st.button("生成 PDF 报告"):
    pdf_file = generate_pdf_report(df)
    with open(pdf_file, "rb") as f:
        st.download_button("下载 PDF", f, file_name="分析报告.pdf", mime="application/pdf")
