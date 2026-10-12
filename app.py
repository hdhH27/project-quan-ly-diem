import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.set_page_config(page_title="Quản lý điểm sinh viên",layout="wide")
st.title("QUẢN LÝ ĐIỂM SINH VIÊN")
st.write("Ứng dụng quản lý điểm, xếp loại và thống kê kết quả học tập.")

# Du lieu mau cua 10 sinh vien
ho_ten = ["An", "Binh", "Chi", "Dung", "Ha", "Lan", "Minh", "Nam", "Phuc", "Trang"]
chuyen_can = [8.0, 9.0, 7.0, 8.5, 7.5, 8.0, 9.0, 7.0, 8.5, 9.0]
giua_ky = [7.5, 8.0, 6.0, 9.0, 7.0, 6.5, 8.5, 7.5, 7.0, 9.0]
cuoi_ky = [8.0, 8.5, 6.5, 9.5, 7.5, 7.0, 8.0, 7.0, 7.5, 9.5]

df = pd.DataFrame({
    "Họ tên": ho_ten,
    "Chuyên cần": chuyen_can,
    "Giữa kỳ": giua_ky,
    "Cuối kỳ": cuoi_ky
})

# Tinh diem tong ket theo cong thuc de bai
df["Tổng kết"] = (0.2 * df["Chuyên cần"] + 0.3 * df["Giữa kỳ"] + 0.5 * df["Cuối kỳ"]).round(2)

def xep_loai(diem):
    if diem >= 8.5:
        return "Giỏi"
    elif diem >= 7.0:
        return "Khá"
    elif diem >= 5.0:
        return "Trung bình"
    else:
        return "Yếu"

df["Xếp loại"] = df["Tổng kết"].apply(xep_loai)

st.subheader(" Bảng điểm của 10 sinh viên")
st.dataframe(df, use_container_width=True, hide_index=True)

st.subheader(" Thống kê kết quả học tập")
diem_tb = df["Tổng kết"].mean()
diem_cao_nhat = df["Tổng kết"].max()
diem_thap_nhat = df["Tổng kết"].min()
so_sinh_vien_dat = int((df["Tổng kết"] >= 5).sum())

c1, c2, c3, c4 = st.columns(4)
c1.metric("Điểm trung bình lớp", f"{diem_tb:.2f}")
c2.metric("Điểm cao nhất", f"{diem_cao_nhat:.2f}")
c3.metric("Điểm thấp nhất", f"{diem_thap_nhat:.2f}")
c4.metric("Số sinh viên đạt", f"{so_sinh_vien_dat}/10")

st.write("**Sinh viên có điểm tổng kết cao nhất:**")
st.write(", ".join(df.loc[df["Tổng kết"] == diem_cao_nhat, "Họ tên"].tolist()))
st.write("**Sinh viên có điểm tổng kết thấp nhất:**")
st.write(", ".join(df.loc[df["Tổng kết"] == diem_thap_nhat, "Họ tên"].tolist()))

st.subheader("🔎 Tra cứu điểm từng sinh viên")
ten_chon = st.selectbox("Chọn sinh viên:", df["Họ tên"].tolist())
sinh_vien = df[df["Họ tên"] == ten_chon].iloc[0]
st.write(f"**Họ tên:** {sinh_vien['Họ tên']}")
a, b, c = st.columns(3)
a.metric("Chuyên cần", f"{sinh_vien['Chuyên cần']:.1f}")
b.metric("Giữa kỳ", f"{sinh_vien['Giữa kỳ']:.1f}")
c.metric("Cuối kỳ", f"{sinh_vien['Cuối kỳ']:.1f}")
d, e = st.columns(2)
d.metric("Điểm tổng kết", f"{sinh_vien['Tổng kết']:.2f}")
e.metric("Xếp loại", sinh_vien["Xếp loại"])

st.subheader("📈 Biểu đồ điểm tổng kết của 10 sinh viên")
fig, ax = plt.subplots(figsize=(10, 5))
ax.barh(df["Họ tên"], df["Tổng kết"], color="cornflowerblue")
ax.set_xlabel("Điểm tổng kết")
ax.set_ylabel("Tên sinh viên")
ax.set_title("Điểm tổng kết của 10 sinh viên")
ax.set_xlim(0, 10)
ax.invert_yaxis()
ax.grid(axis="x", linestyle="--", alpha=0.3)
fig.tight_layout()
st.pyplot(fig)
plt.close(fig)

st.caption("Công thức: 20% Chuyên cần + 30% Giữa kỳ + 50% Cuối kỳ.")
st.divider()
st.caption("Người thực hiện: NGUYEN VAN A | MSSV: 00000000")
