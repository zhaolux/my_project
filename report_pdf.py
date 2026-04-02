from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
import matplotlib.pyplot as plt

def generate_pdf_report(df, filename="分析报告.pdf"):
    c = canvas.Canvas(filename, pagesize=A4)
    width, height = A4

    c.setFont("Helvetica-Bold", 20)
    c.drawCentredString(width/2, height-50, "📊 数据分析报告")

    total = df["quantity"].sum()
    avg = df["quantity"].mean()
    top = df.groupby("product")["quantity"].sum().idxmax()

    c.setFont("Helvetica", 12)
    c.drawString(50, height-100, f"总销量: {total}")
    c.drawString(50, height-120, f"平均销量: {avg:.2f}")
    c.drawString(50, height-140, f"最畅销商品: {top}")

    # 图表
    plt.figure(figsize=(4,3))
    sales = df.groupby("product")["quantity"].sum()
    sales.plot(kind="bar", title="分类销量")
    plt.tight_layout()
    plt.savefig("temp_chart.png")
    plt.close()

    c.drawImage("temp_chart.png", 50, height-400, width=400, height=250)
    c.showPage()
    c.save()
    return filename
