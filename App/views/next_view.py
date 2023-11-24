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


def NextView(page:ft.Page,params:Params,basket:Basket):

    page.title=("Vektor dan Nilai Eigen")
    page.bgcolor= ft.colors.WHITE
    page.scroll = ft.ScrollMode.AUTO    

    copy = ft.Container(
                alignment=ft.alignment.bottom_left,
                content = ft.Text("Copyright ©2023 Kelompok 5B Aljabar Linear dan Matriks", color=ft.colors.BLACK))


    judul = ft.Container(
                    alignment=ft.alignment.center,
                    content=ft.Text("Nilai dan Vektor Eigen",
                     font_family="Impact",  
                      style=ft.TextThemeStyle.TITLE_LARGE,
                      color=ft.colors.RED,
                        ))
    

    a = ft.Container(alignment=ft.alignment.center, content=ft.Text("Dari Data di atas didapatlah:" , color=ft.colors.RED, font_family="Impact"))
    
    kesimpulan = ft.Container(alignment=ft.alignment.center, content=ft.Text((f"Berdasarkan perhitungan nilai dan vektor eigen, maka didapatlah kesimpulan bahwa {max(result, key=result.get)} Menjadi kampus terbaik di Tasikmalaya dengan persentase {100*max(veigen):2f}%") , color=ft.colors.RED, font_family="Impact"))
    
    spasi = ft.Container(ft.Text(""))



    

    def keluar(e):
        page.window_close()
    keluar = ft.Container(
                alignment=ft.alignment.bottom_right,
                content=ft.ElevatedButton(text="Exit",
                width=75,
                height=37,
                bgcolor=ft.colors.RED,
                color=ft.colors.WHITE,
                expand=0,
                on_click=keluar))
    
    
    hasil = ft.Container(
        alignment=ft.alignment.center,
        content=ft.DataTable(
            data_row_height=40,
            heading_row_height=40,
            columns=[
                ft.DataColumn(ft.Text("Unsil", color=ft.colors.BLACK, font_family="Impact")),
                ft.DataColumn(ft.Text(f":   {100*veigen1:.2f}%", color=ft.colors.BLACK, font_family="Impact")),
            ],
            rows=[
                ft.DataRow(
                    cells=[
                        ft.DataCell(ft.Text("Unper", color=ft.colors.BLACK, font_family="Impact")),
                        ft.DataCell(ft.Text(f":  {100*veigen2:.2f}%", color=ft.colors.BLACK, font_family="Impact")),
                    ],
                ),
                ft.DataRow(
                    cells=[
                        ft.DataCell(ft.Text("Umtas", color=ft.colors.BLACK, font_family="Impact")),
                        ft.DataCell(ft.Text(f":  {100*veigen3:.2f}%", color=ft.colors.BLACK, font_family="Impact")),
                    ],
                ),
                ft.DataRow(
                    cells=[
                        ft.DataCell(ft.Text("Upi Tasik", color=ft.colors.BLACK, font_family="Impact")),
                        ft.DataCell(ft.Text(f":  {100*veigen5:.2f}%", color=ft.colors.BLACK, font_family="Impact")),
                    ],
                ),
                ft.DataRow(
                    cells=[
                        ft.DataCell(ft.Text("BTH", color=ft.colors.BLACK, font_family="Impact")),
                        ft.DataCell(ft.Text(f":  {100*veigen4:.2f}%", color=ft.colors.BLACK, font_family="Impact")),
                    ],
                ),
                ft.DataRow(
                    cells=[
                        ft.DataCell(ft.Text("STAI", color=ft.colors.BLACK, font_family="Impact")),
                        ft.DataCell(ft.Text(f":  {100*veigen6:.2f}%", color=ft.colors.BLACK, font_family="Impact")),
                    ],
                ),
            ],
        ),)
    

    
    data = ft.Container(
                    alignment=ft.alignment.center,
                    content=ft.DataTable(
                    data_row_height=30,
            columns=[
                ft.DataColumn(ft.Text("")),
                ft.DataColumn(ft.Text("Unsil", color=ft.colors.BLACK, font_family="Impact")),
                ft.DataColumn(ft.Text("Unper", color=ft.colors.BLACK, font_family="Impact")),
                ft.DataColumn(ft.Text("Umtas", color=ft.colors.BLACK, font_family="Impact")),
                ft.DataColumn(ft.Text("BTH", color=ft.colors.BLACK, font_family="Impact")),
                ft.DataColumn(ft.Text("UPI", color=ft.colors.BLACK, font_family="Impact")),
                ft.DataColumn(ft.Text("STAI", color=ft.colors.BLACK, font_family="Impact")),
                ft.DataColumn(ft.Text("V. Eigen", color=ft.colors.BLACK, font_family="Impact"))
            ],
            rows=[
                ft.DataRow(
                    cells=[
                        ft.DataCell(ft.Text("Unsil", color=ft.colors.BLACK, font_family="Impact")),
                        ft.DataCell(ft.Text(nilai1, color=ft.colors.BLACK, font_family="Impact")),
                        ft.DataCell(ft.Text(nilai7, color=ft.colors.BLACK, font_family="Impact")),
                        ft.DataCell(ft.Text(nilai13, color=ft.colors.BLACK, font_family="Impact")),
                        ft.DataCell(ft.Text(nilai19, color=ft.colors.BLACK, font_family="Impact")),
                        ft.DataCell(ft.Text(nilai25, color=ft.colors.BLACK, font_family="Impact")),
                        ft.DataCell(ft.Text(nilai31, color=ft.colors.BLACK, font_family="Impact")),
                        ft.DataCell(ft.Text(veigen1, color=ft.colors.BLACK, font_family="Impact"))
                    ],
                ),
                ft.DataRow(
                    cells=[
                        ft.DataCell(ft.Text("Unper", color=ft.colors.BLACK, font_family="Impact")),
                        ft.DataCell(ft.Text(nilai2, color=ft.colors.BLACK, font_family="Impact")),
                        ft.DataCell(ft.Text(nilai8, color=ft.colors.BLACK, font_family="Impact")),
                        ft.DataCell(ft.Text(nilai14, color=ft.colors.BLACK, font_family="Impact")),
                        ft.DataCell(ft.Text(nilai20, color=ft.colors.BLACK, font_family="Impact")),
                        ft.DataCell(ft.Text(nilai26, color=ft.colors.BLACK, font_family="Impact")),
                        ft.DataCell(ft.Text(nilai31, color=ft.colors.BLACK, font_family="Impact")),
                        ft.DataCell(ft.Text(veigen2, color=ft.colors.BLACK, font_family="Impact"))
                    ],
                ),
                ft.DataRow(
                    cells=[
                        ft.DataCell(ft.Text("Umtas",  color=ft.colors.BLACK, font_family="Impact")),
                        ft.DataCell(ft.Text(nilai3, color=ft.colors.BLACK, font_family="Impact")),
                        ft.DataCell(ft.Text(nilai9, color=ft.colors.BLACK, font_family="Impact")),
                        ft.DataCell(ft.Text(nilai15, color=ft.colors.BLACK, font_family="Impact")),
                        ft.DataCell(ft.Text(nilai21, color=ft.colors.BLACK, font_family="Impact")),
                        ft.DataCell(ft.Text(nilai27, color=ft.colors.BLACK, font_family="Impact")),
                        ft.DataCell(ft.Text(nilai32, color=ft.colors.BLACK, font_family="Impact")),
                        ft.DataCell(ft.Text(veigen3, color=ft.colors.BLACK, font_family="Impact"))
                    ],
                ),
                ft.DataRow(
                    cells=[
                        ft.DataCell(ft.Text("BTH",  color=ft.colors.BLACK, font_family="Impact")),
                        ft.DataCell(ft.Text(nilai4, color=ft.colors.BLACK, font_family="Impact")),
                        ft.DataCell(ft.Text(nilai10, color=ft.colors.BLACK, font_family="Impact")),
                        ft.DataCell(ft.Text(nilai16, color=ft.colors.BLACK, font_family="Impact")),
                        ft.DataCell(ft.Text(nilai22, color=ft.colors.BLACK, font_family="Impact")),
                        ft.DataCell(ft.Text(nilai28, color=ft.colors.BLACK, font_family="Impact")),
                        ft.DataCell(ft.Text(nilai33, color=ft.colors.BLACK, font_family="Impact")),
                        ft.DataCell(ft.Text(veigen4, color=ft.colors.BLACK, font_family="Impact"))
                    ],
                ),
                ft.DataRow(
                    cells=[
                        ft.DataCell(ft.Text("UPI Tasik",  color=ft.colors.BLACK, font_family="Impact")),
                        ft.DataCell(ft.Text(nilai5, color=ft.colors.BLACK, font_family="Impact")),
                        ft.DataCell(ft.Text(nilai11, color=ft.colors.BLACK, font_family="Impact")),
                        ft.DataCell(ft.Text(nilai17, color=ft.colors.BLACK, font_family="Impact")),
                        ft.DataCell(ft.Text(nilai23, color=ft.colors.BLACK, font_family="Impact")),
                        ft.DataCell(ft.Text(nilai29, color=ft.colors.BLACK, font_family="Impact")),
                        ft.DataCell(ft.Text(nilai34, color=ft.colors.BLACK, font_family="Impact")),
                        ft.DataCell(ft.Text(veigen5, color=ft.colors.BLACK, font_family="Impact"))
                    ],
                ),
                ft.DataRow(
                    cells=[
                        ft.DataCell(ft.Text("STAI",  color=ft.colors.BLACK, font_family="Impact")),
                        ft.DataCell(ft.Text(nilai6, color=ft.colors.BLACK, font_family="Impact")),
                        ft.DataCell(ft.Text(nilai12, color=ft.colors.BLACK, font_family="Impact")),
                        ft.DataCell(ft.Text(nilai18, color=ft.colors.BLACK, font_family="Impact")),
                        ft.DataCell(ft.Text(nilai24, color=ft.colors.BLACK, font_family="Impact")),
                        ft.DataCell(ft.Text(nilai30, color=ft.colors.BLACK, font_family="Impact")),
                        ft.DataCell(ft.Text(nilai36, color=ft.colors.BLACK, font_family="Impact")),
                        ft.DataCell(ft.Text(veigen6, color=ft.colors.BLACK, font_family="Impact"))
                    ],
                ),
            ],
        ),)

    kembali = ft.ElevatedButton("<", on_click=lambda _: page.go("/"), bgcolor=ft.colors.RED, color=ft.colors.WHITE)
    page.window_center()
    page.window_bgcolor = ft.colors.WHITE
    page.window_title_bar_hidden = True
    page.window_width=850
    page.window_height=660
    jud = ft.Row(controls=[kembali, judul], spacing=250)
    footer = ft.Container(ft.Row(controls=[copy, keluar], spacing=365))


    return ft.View(
        "/next_view/:my_id",
        controls=[
           jud, data, spasi, a, hasil, footer,
        ]
    )
