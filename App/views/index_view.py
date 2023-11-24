import flet as ft
from flet_route import Params,Basket
import numpy as np

# Matriks Perbandingan
penilaian = np.array([  [1, 4, 4, 3, 1/2, 4],
                        [1/4, 1, 1/2, 2, 1/3, 1],
                        [1/4, 2, 1, 2, 1/3, 1],
                        [1/3, 1/2, 1/2, 1, 1/3, 2],
                        [2, 3, 3, 3, 1, 3],
                        [1/4, 1, 1, 1/2, 1/2, 1]])

#Mencari Nilai Eigen
total_kolom = np.sum(penilaian, axis=0)
eigen = penilaian/total_kolom

#Mencari Vektor Eigen
veigen = np.mean(eigen, axis=1)


#Memasukkan Matriks Hasil Eigen dan Vektor Eigen ke dalam Variabel
#Agar Lebih Mudah Dipanggil saat Membuat Interface

nilai1 = np.round((eigen[0][0]), decimals=3)
nilai2 =  np.round((eigen[1][0]), decimals=3)
nilai3 =  np.round((eigen[2][0]), decimals=3)
nilai4 =  np.round((eigen[3][0]), decimals=3)
nilai5 =  np.round((eigen[4][0]), decimals=3)
nilai6 =  np.round((eigen[5][0]), decimals=3)
nilai7 =  np.round((eigen[0][1]), decimals=3)
nilai8 =  np.round((eigen[1][1]), decimals=3)
nilai9 =  np.round((eigen[2][1]), decimals=3)
nilai10 =  np.round((eigen[3][1]), decimals=3)
nilai11 =  np.round((eigen[4][1]) , decimals=3)
nilai12 =  np.round((eigen[5][1]), decimals=3)
nilai13 =  np.round((eigen[0][2]), decimals=3)
nilai14 =  np.round((eigen[1][2]), decimals=3)
nilai15 =  np.round((eigen[2][2]), decimals=3)
nilai16 =  np.round((eigen[3][2]), decimals=3)
nilai17 =  np.round((eigen[4][2]), decimals=3)
nilai18 =  np.round((eigen[5][2]), decimals=3)
nilai19 =  np.round((eigen[0][3]), decimals=3)
nilai20 =  np.round((eigen[1][3]), decimals=3)
nilai21 =  np.round((eigen[2][3]), decimals=3)
nilai22 =  np.round((eigen[3][3]), decimals=3)
nilai23 =  np.round((eigen[4][3]), decimals=3)
nilai24 =  np.round((eigen[5][3]), decimals=3)
nilai25 =  np.round((eigen[0][4]), decimals=3)
nilai26 =  np.round((eigen[1][4]), decimals=3)
nilai27 =  np.round((eigen[2][4]), decimals=3)
nilai28 =  np.round((eigen[3][4]), decimals=3)
nilai29 =  np.round((eigen[4][4]), decimals=3)
nilai30 =  np.round((eigen[5][4]), decimals=3)
nilai31 =  np.round((eigen[0][5]), decimals=3)
nilai32 =  np.round((eigen[1][5]), decimals=3)
nilai33 =  np.round((eigen[2][5]), decimals=3)
nilai34 =  np.round((eigen[3][5]), decimals=3)
nilai35 =  np.round((eigen[4][5]), decimals=3)
nilai36 =  np.round((eigen[5][5]), decimals=3)

veigen1 =  np.round((veigen[0]), decimals=3)
veigen2 =  np.round((veigen[1]), decimals=3)
veigen3 =  np.round((veigen[2]), decimals=3)
veigen4 =  np.round((veigen[3]), decimals=3)
veigen5 =  np.round((veigen[4]), decimals=3)
veigen6 =  np.round((veigen[5]), decimals=3)

label = ['Universitas Siliwangi', 'Universitas perjuangan', 'Universitas Muhammadiyah Tasikmalaya', 'Universitas BTH', 'UPI Kampus Tasikmalaya', 'STAI Tasikmalaya']
isi = [veigen1, veigen2, veigen3, veigen4, veigen5, veigen6]
result = { label: value for label, value in zip(label, isi) }




def IndexView(page:ft.Page,params:Params,basket:Basket):
    page.window_center()
    page.window_title_bar_hidden = True
    page.theme_mode = ft.ThemeMode.LIGHT
    page.window_width=750
    page.window_height=150
    kesimpulan = ft.Container(alignment=ft.alignment.center, content=ft.Text((f"Berdasarkan Matriks Perbandingan yang diberikan, didapatkan kesimpulan bahwa {max(result, key=result.get)} Menjadi kampus terbaik di Tasikmalaya dengan persentase {100*max(veigen):2f}%") , color=ft.colors.RED, font_family="Impact", text_align=ft.TextAlign.CENTER))
    
    return ft.View(
        "/",
        controls=[
            kesimpulan,
            ft.Container(alignment=ft.alignment.bottom_center,content=(ft.ElevatedButton("Lihat Pembahasan ->" ,on_click=lambda _: page.go("/next_view/10")))),
        ]
    )
