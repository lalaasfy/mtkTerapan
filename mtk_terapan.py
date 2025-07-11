# Import pustaka yang diperlukan
import streamlit as st             # Untuk membuat aplikasi web interaktif
import sympy as sp                # Untuk perhitungan simbolik (turunan, integral, dll.)
import numpy as np                # Untuk manipulasi array dan perhitungan numerik
import matplotlib.pyplot as plt   # Untuk membuat grafik

# Judul aplikasi
st.title("🔢 Kalkulator Integral dan Turunan")

# Deskripsi aplikasi dengan Markdown
st.markdown("Aplikasi ini menghitung *turunan* dan *integral* dari fungsi aljabar.")

# Input teks dari pengguna untuk fungsi matematika
fungsi_input = st.text_input("Masukkan fungsi f(x):", value="x**2 + 3*x - 5")

# Membuat simbol x yang akan digunakan dalam ekspresi simbolik
x = sp.symbols('x')

try:
    # Mengubah string input dari pengguna menjadi ekspresi simbolik
    fungsi = sp.sympify(fungsi_input)

    # Menghitung turunan dari fungsi terhadap x
    turunan = sp.diff(fungsi, x)

    # Menghitung integral tak tentu dari fungsi terhadap x
    integral = sp.integrate(fungsi, x)

    # Menampilkan hasil turunan dan integral menggunakan format LaTeX
    st.write("### 🔽 Hasil:")
    st.latex(f"f(x) = {sp.latex(fungsi)}")
    st.latex(f"f'(x) = {sp.latex(turunan)}")
    st.latex(f"\\int f(x) dx = {sp.latex(integral)} + C")  # '+ C' menunjukkan konstanta integrasi

    # Input numerik untuk mengevaluasi nilai fungsi dan turunannya di titik tertentu
    nilai_x = st.number_input("Evaluasi pada x =", value=1.0)

    # Menghitung nilai fungsi dan turunannya di titik tersebut (secara numerik)
    nilai_fungsi = fungsi.subs(x, nilai_x).evalf()
    nilai_turunan = turunan.subs(x, nilai_x).evalf()

    # Menampilkan hasil evaluasi numerik
    st.write(f"f({nilai_x}) = {nilai_fungsi}")
    st.write(f"f'({nilai_x}) = {nilai_turunan}")

    # Menampilkan grafik fungsi dan turunannya
    st.write("### 📈 Grafik Fungsi dan Turunan")

    # Membuat array nilai x dari -10 sampai 10 dengan 400 titik
    x_vals = np.linspace(-10, 10, 400)

    # Mengubah fungsi simbolik menjadi fungsi numerik (agar bisa dipakai oleh numpy)
    f_lambd = sp.lambdify(x, fungsi, "numpy")
    d_lambd = sp.lambdify(x, turunan, "numpy")

    # Membuat plot fungsi dan turunan
    plt.figure(figsize=(8, 4))
    plt.plot(x_vals, f_lambd(x_vals), label='f(x)', color='blue')            # Garis fungsi utama
    plt.plot(x_vals, d_lambd(x_vals), label="f'(x)", linestyle='--', color='red')  # Garis turunan
    plt.title("Grafik f(x) dan f'(x)")         # Judul grafik
    plt.xlabel("x")                            # Label sumbu X
    plt.ylabel("y")                            # Label sumbu Y
    plt.legend()                               # Menampilkan legenda
    plt.grid(True)                             # Menampilkan grid
    st.pyplot(plt.gcf())                       # Menampilkan plot di Streamlit

# Menangani kesalahan input (misalnya jika input tidak valid)
except Exception as e:
    st.error(f"Terjadi kesalahan dalam input fungsi: {e}")
