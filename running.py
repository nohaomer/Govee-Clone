import pandas as pd
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import time
import datetime
import csv
import random
from PIL import Image


class no:
    # used in second page to sent combobox value
    def __init__(self, n, z):
        self.n = n
        self.z = z
        print(self.n)

    DATA1 = []
    DATA1_hum = []
    DATA2 = []
    DATA2_hum = []
    DATA3 = []
    DATA3_hum = []
    DATA4 = []
    DATA4_hum = []
    DATA5 = []
    DATA5_hum = []
    DATA6 = []
    DATA6_hum = []
    DATA7 = []
    DATA7_hum = []
    DATA8 = []
    DATA8_hum = []
    DATA9 = []
    DATA9_hum = []
    DATA10 = []
    DATA10_hum = []
    DATA11 = []
    DATA11_hum = []
    DATA12 = []
    DATA12_hum = []
    DATA13 = []
    DATA13_hum = []
    DATA14 = []
    DATA14_hum = []
    DATA15 = []
    DATA15_hum = []
    DATA16 = []
    DATA16_hum = []
    DATA17 = []
    DATA17_hum = []
    DATA18 = []
    DATA18_hum = []

    def noha(temp_file, hum_file, a):
        current_time = datetime.datetime.now()
        # t =str(current_time.hour) + ":" + str(current_time.minute)
        t = str(current_time.date()) + "-" + str(current_time.hour) + ":" + str(current_time.minute)
        DATA1 = [t, str(round(random.uniform(18, 23), 2))],
        DATA1_hum = [t, str(round(random.uniform(43.5, 55), 2))],  # 2 to write 2 digit only after point as 74.25
        DATA2 = [t, str(round(random.uniform(18.5, 22.5), 2))],
        DATA2_hum = [t, str(round(random.uniform(41.9, 55.3), 2))],
        DATA3 = [t, str(round(random.uniform(18.03, 21.87), 2))],
        DATA3_hum = [t, str(round(random.uniform(42.1, 55.5), 2))],
        DATA4 = [t, str(round(random.uniform(18.25, 21.99), 2))],
        DATA4_hum = [t, str(round(random.uniform(45, 56.2), 2))],
        DATA5 = [t, str(round(random.uniform(18.09, 22.77), 2))],
        DATA5_hum = [t, str(round(random.uniform(44.8, 57), 2))],
        DATA6 = [t, str(round(random.uniform(19, 21.5), 2))],
        DATA6_hum = [t, str(round(random.uniform(40, 50), 2))],
        DATA7 = [t, str(round(random.uniform(18.05, 22), 2))],
        DATA7_hum = [t, str(round(random.uniform(42.5, 54), 2))],
        DATA8 = [t, str(round(random.uniform(18.37, 21.65), 2))],
        DATA8_hum = [t, str(round(random.uniform(43.1, 52.5), 2))],
        DATA9 = [t, str(round(random.uniform(18.55, 21.9), 2))],
        DATA9_hum = [t, str(round(random.uniform(41, 54.6), 2))],
        DATA10 = [t, str(round(random.uniform(19, 21.44), 2))],
        DATA10_hum = [t, str(round(random.uniform(42.9, 53.5), 2))],
        DATA11 = [t, str(round(random.uniform(18.77, 22.3), 2))],
        DATA11_hum = [t, str(round(random.uniform(43, 54.8), 2))],
        DATA12 = [t, str(round(random.uniform(18.83, 22.33), 2))],
        DATA12_hum = [t, str(round(random.uniform(44.5, 53), 2))],
        DATA13 = [t, str(round(random.uniform(18.07, 22.01), 2))],
        DATA13_hum = [t, str(round(random.uniform(42, 54.9), 2))],
        DATA14 = [t, str(round(random.uniform(18.1, 22.35), 2))],
        DATA14_hum = [t, str(round(random.uniform(40.5, 52), 2))],
        DATA15 = [t, str(round(random.uniform(39, 40.5), 2))],
        DATA15_hum = [t, str(round(random.uniform(74, 75), 2))],
        DATA16 = [t, str(round(random.uniform(29, 30.2), 2))],
        DATA16_hum = [t, str(round(random.uniform(64, 65), 2))],
        DATA17 = [t, str(round(random.uniform(2, 4), 2))],
        DATA17_hum = [t, str(round(random.uniform(60, 80), 2))],
        DATA18 = [t, str(round(random.uniform(-18, -22), 2))],
        DATA18_hum = [t, str(round(random.uniform(60, 75), 2))],
        DATA19 = [t, str(round(random.uniform(22.4, 22.6), 2))],
        DATA19_hum = [t, str(round(random.uniform(44, 46), 2))],
        DATA20 = [t, str(round(random.uniform(32.40, 32.60), 2))],
        DATA20_hum = [t, str(round(random.uniform(44, 46), 2))],
        DATA21 = [t, str(round(random.uniform(32.50, 33.60), 2))],
        DATA21_hum = [t, str(round(random.uniform(47.50, 50), 2))],
        DATA22 = [t, str(round(random.uniform(52.5, 54), 2))],
        DATA22_hum = [t, str(round(random.uniform(47.5, 50), 2))],
        DATA23 = [t, str(round(random.uniform(18, 23), 2))],
        DATA23_hum = [t, str(round(random.uniform(40, 52), 2))],
        DATA24 = [t, str(round(random.uniform(18.09, 22.77), 2))],
        DATA24_hum = [t, str(round(random.uniform(44.8, 54), 2))],
        DATA25 = [t, str(round(random.uniform(39.4, 40.4), 2))],
        DATA25_hum = [t, str(round(random.uniform(74, 75), 2))],
        DATA26 = [t, str(round(random.uniform(29.8, 30.2), 2))],
        DATA26_hum = [t, str(round(random.uniform(64, 65), 2))],
        DATA27 = [t, str(round(random.uniform(3, 8), 2))],
        DATA27_hum = [t, str(round(random.uniform(60, 80), 2))],
        DATA28 = [t, str(round(random.uniform(2, 7.9), 2))],
        DATA28_hum = [t, str(round(random.uniform(50, 90), 2))],
        DATA29 = [t, str(round(random.uniform(19, 23), 2))],
        DATA29_hum = [t, str(round(random.uniform(40, 50), 2))],
        DATA30 = [t, str(round(random.uniform(18, 23), 2))],
        DATA30_hum = [t, str(round(random.uniform(40, 52), 2))],
        DATA31 = [t, str(round(random.uniform(2, 6.5), 2))],
        DATA31_hum = [t, str(round(random.uniform(60, 80), 2))],
        DATA32 = [t, str(round(random.uniform(21.4, 22.6), 2))],
        DATA32_hum = [t, str(round(random.uniform(40, 60), 2))],
        DATA33 = [t, str(round(random.uniform(31.40, 32.60), 2))],
        DATA33_hum = [t, str(round(random.uniform(40, 60), 2))],
        DATA34 = [t, str(round(random.uniform(31.50, 33.60), 2))],
        DATA34_hum = [t, str(round(random.uniform(30, 40), 2))],
        DATA35 = [t, str(round(random.uniform(52.5, 54), 2))],
        DATA35_hum = [t, str(round(random.uniform(10, 40), 2))],
        DATA36 = [t, str(round(random.uniform(18, 23), 2))],
        DATA36_hum = [t, str(round(random.uniform(40, 53), 2))],
        DATA37 = [t, str(round(random.uniform(18.7, 20.7), 2))],
        DATA37_hum = [t, str(round(random.uniform(40, 55), 2))],
        DATA38 = [t, str(round(random.uniform(21.5, 23), 2))],
        DATA38_hum = [t, str(round(random.uniform(40, 55), 2))],


        print(1)
        if a == 1:

            with open(temp_file, 'a+', encoding='UTF8', newline='') as f:  # a+ ------> append
                writer = csv.writer(f)
                writer.writerows(DATA1)
            with open(hum_file, 'a+', encoding='UTF8', newline='') as f:  # a+ ------> append
                writer = csv.writer(f)
                writer.writerows(DATA1_hum)

        elif a == 2:

            with open(temp_file, 'a+', encoding='UTF8', newline='') as f:  # a+ ------> append
                writer = csv.writer(f)
                writer.writerows(DATA2)
            with open(hum_file, 'a+', encoding='UTF8', newline='') as f:  # a+ ------> append
                writer = csv.writer(f)
                writer.writerows(DATA2_hum)

        elif a == 3:

            with open(temp_file, 'a+', encoding='UTF8', newline='') as f:  # a+ ------> append
                writer = csv.writer(f)
                writer.writerows(DATA3)
            with open(hum_file, 'a+', encoding='UTF8', newline='') as f:  # a+ ------> append
                writer = csv.writer(f)
                writer.writerows(DATA3_hum)

        elif a == 4:
            with open(temp_file, 'a+', encoding='UTF8', newline='') as f:  # a+ ------> append
                writer = csv.writer(f)
                writer.writerows(DATA4)
            with open(hum_file, 'a+', encoding='UTF8', newline='') as f:  # a+ ------> append
                writer = csv.writer(f)
                writer.writerows(DATA4_hum)

        elif a == 5:
            with open(temp_file, 'a+', encoding='UTF8', newline='') as f:  # a+ ------> append
                writer = csv.writer(f)
                writer.writerows(DATA5)
            with open(hum_file, 'a+', encoding='UTF8', newline='') as f:  # a+ ------> append
                writer = csv.writer(f)
                writer.writerows(DATA5_hum)
        elif a == 6:
            with open(temp_file, 'a+', encoding='UTF8', newline='') as f:  # a+ ------> append
                writer = csv.writer(f)
                writer.writerows(DATA6)
            with open(hum_file, 'a+', encoding='UTF8', newline='') as f:  # a+ ------> append
                writer = csv.writer(f)
                writer.writerows(DATA6_hum)
        elif a == 7:
            with open(temp_file, 'a+', encoding='UTF8', newline='') as f:  # a+ ------> append
                writer = csv.writer(f)
                writer.writerows(DATA7)
            with open(hum_file, 'a+', encoding='UTF8', newline='') as f:  # a+ ------> append
                writer = csv.writer(f)
                writer.writerows(DATA7_hum)
        elif a == 8:
            with open(temp_file, 'a+', encoding='UTF8', newline='') as f:  # a+ ------> append
                writer = csv.writer(f)
                writer.writerows(DATA8)
            with open(hum_file, 'a+', encoding='UTF8', newline='') as f:  # a+ ------> append
                writer = csv.writer(f)
                writer.writerows(DATA8_hum)

        elif a == 8:
            with open(temp_file, 'a+', encoding='UTF8', newline='') as f:  # a+ ------> append
                writer = csv.writer(f)
                writer.writerows(DATA8)
            with open(hum_file, 'a+', encoding='UTF8', newline='') as f:  # a+ ------> append
                writer = csv.writer(f)
                writer.writerows(DATA8_hum)

        elif a == 9:
            with open(temp_file, 'a+', encoding='UTF8', newline='') as f:  # a+ ------> append
                writer = csv.writer(f)
                writer.writerows(DATA9)
            with open(hum_file, 'a+', encoding='UTF8', newline='') as f:  # a+ ------> append
                writer = csv.writer(f)
                writer.writerows(DATA9_hum)

        elif a == 10:
            with open(temp_file, 'a+', encoding='UTF8', newline='') as f:  # a+ ------> append
                writer = csv.writer(f)
                writer.writerows(DATA10)
            with open(hum_file, 'a+', encoding='UTF8', newline='') as f:  # a+ ------> append
                writer = csv.writer(f)
                writer.writerows(DATA10_hum)
        elif a == 11:
            with open(temp_file, 'a+', encoding='UTF8', newline='') as f:  # a+ ------> append
                writer = csv.writer(f)
                writer.writerows(DATA11)
            with open(hum_file, 'a+', encoding='UTF8', newline='') as f:  # a+ ------> append
                writer = csv.writer(f)
                writer.writerows(DATA11_hum)

        elif a == 12:
            with open(temp_file, 'a+', encoding='UTF8', newline='') as f:  # a+ ------> append
                writer = csv.writer(f)
                writer.writerows(DATA12)
            with open(hum_file, 'a+', encoding='UTF8', newline='') as f:  # a+ ------> append
                writer = csv.writer(f)
                writer.writerows(DATA12_hum)
            # print("hello")
        elif a == 13:
            with open(temp_file, 'a+', encoding='UTF8', newline='') as f:  # a+ ------> append
                writer = csv.writer(f)
                writer.writerows(DATA13)
            with open(hum_file, 'a+', encoding='UTF8', newline='') as f:  # a+ ------> append
                writer = csv.writer(f)
                writer.writerows(DATA13_hum)

        elif a == 14:
            with open(temp_file, 'a+', encoding='UTF8', newline='') as f:  # a+ ------> append
                writer = csv.writer(f)
                writer.writerows(DATA14)
            with open(hum_file, 'a+', encoding='UTF8', newline='') as f:  # a+ ------> append
                writer = csv.writer(f)
                writer.writerows(DATA14_hum)
        elif a == 15:
            with open(temp_file, 'a+', encoding='UTF8', newline='') as f:  # a+ ------> append
                writer = csv.writer(f)
                writer.writerows(DATA15)
            with open(hum_file, 'a+', encoding='UTF8', newline='') as f:  # a+ ------> append
                writer = csv.writer(f)
                writer.writerows(DATA15_hum)
        elif a == 16:
            with open(temp_file, 'a+', encoding='UTF8', newline='') as f:  # a+ ------> append
                writer = csv.writer(f)
                writer.writerows(DATA16)
            with open(hum_file, 'a+', encoding='UTF8', newline='') as f:  # a+ ------> append
                writer = csv.writer(f)
                writer.writerows(DATA16_hum)

        elif a == 17:
            with open(temp_file, 'a+', encoding='UTF8', newline='') as f:  # a+ ------> append
                writer = csv.writer(f)
                writer.writerows(DATA17)
            with open(hum_file, 'a+', encoding='UTF8', newline='') as f:  # a+ ------> append
                writer = csv.writer(f)
                writer.writerows(DATA17_hum)

        elif a == 18:
            with open(temp_file, 'a+', encoding='UTF8', newline='') as f:  # a+ ------> append
                writer = csv.writer(f)
                writer.writerows(DATA18)
            with open(hum_file, 'a+', encoding='UTF8', newline='') as f:  # a+ ------> append
                writer = csv.writer(f)
                writer.writerows(DATA18_hum)

        elif a == 19:
            with open(temp_file, 'a+', encoding='UTF8', newline='') as f:  # a+ ------> append
                writer = csv.writer(f)
                writer.writerows(DATA19)
            with open(hum_file, 'a+', encoding='UTF8', newline='') as f:  # a+ ------> append
                writer = csv.writer(f)
                writer.writerows(DATA19_hum)
        elif a == 20:
            with open(temp_file, 'a+', encoding='UTF8', newline='') as f:  # a+ ------> append
                writer = csv.writer(f)
                writer.writerows(DATA20)
            with open(hum_file, 'a+', encoding='UTF8', newline='') as f:  # a+ ------> append
                writer = csv.writer(f)
                writer.writerows(DATA20_hum)
        elif a == 21:
            with open(temp_file, 'a+', encoding='UTF8', newline='') as f:  # a+ ------> append
                writer = csv.writer(f)
                writer.writerows(DATA21)
            with open(hum_file, 'a+', encoding='UTF8', newline='') as f:  # a+ ------> append
                writer = csv.writer(f)
                writer.writerows(DATA22_hum)
        elif a == 22:
            with open(temp_file, 'a+', encoding='UTF8', newline='') as f:  # a+ ------> append
                writer = csv.writer(f)
                writer.writerows(DATA22)
            with open(hum_file, 'a+', encoding='UTF8', newline='') as f:  # a+ ------> append
                writer = csv.writer(f)
                writer.writerows(DATA22_hum)
        elif a == 23:
            with open(temp_file, 'a+', encoding='UTF8', newline='') as f:  # a+ ------> append
                writer = csv.writer(f)
                writer.writerows(DATA23)
            with open(hum_file, 'a+', encoding='UTF8', newline='') as f:  # a+ ------> append
                writer = csv.writer(f)
                writer.writerows(DATA23_hum)
        elif a == 24:
            with open(temp_file, 'a+', encoding='UTF8', newline='') as f:  # a+ ------> append
                writer = csv.writer(f)
                writer.writerows(DATA24)
            with open(hum_file, 'a+', encoding='UTF8', newline='') as f:  # a+ ------> append
                writer = csv.writer(f)
                writer.writerows(DATA24_hum)
        elif a == 25:
            with open(temp_file, 'a+', encoding='UTF8', newline='') as f:  # a+ ------> append
                writer = csv.writer(f)
                writer.writerows(DATA25)
            with open(hum_file, 'a+', encoding='UTF8', newline='') as f:  # a+ ------> append
                writer = csv.writer(f)
                writer.writerows(DATA25_hum)

        elif a == 26:
            with open(temp_file, 'a+', encoding='UTF8', newline='') as f:  # a+ ------> append
                writer = csv.writer(f)
                writer.writerows(DATA26)
            with open(hum_file, 'a+', encoding='UTF8', newline='') as f:  # a+ ------> append
                writer = csv.writer(f)
                writer.writerows(DATA26_hum)
        elif a == 27:
            with open(temp_file, 'a+', encoding='UTF8', newline='') as f:  # a+ ------> append
                writer = csv.writer(f)
                writer.writerows(DATA27)
            with open(hum_file, 'a+', encoding='UTF8', newline='') as f:  # a+ ------> append
                writer = csv.writer(f)
                writer.writerows(DATA27_hum)
        elif a == 28:
            with open(temp_file, 'a+', encoding='UTF8', newline='') as f:  # a+ ------> append
                writer = csv.writer(f)
                writer.writerows(DATA28)
            with open(hum_file, 'a+', encoding='UTF8', newline='') as f:  # a+ ------> append
                writer = csv.writer(f)
                writer.writerows(DATA28_hum)
        elif a == 29:
            with open(temp_file, 'a+', encoding='UTF8', newline='') as f:  # a+ ------> append
                writer = csv.writer(f)
                writer.writerows(DATA29)
            with open(hum_file, 'a+', encoding='UTF8', newline='') as f:  # a+ ------> append
                writer = csv.writer(f)
                writer.writerows(DATA29_hum)

        elif a == 30:
            with open(temp_file, 'a+', encoding='UTF8', newline='') as f:  # a+ ------> append
                writer = csv.writer(f)
                writer.writerows(DATA30)
            with open(hum_file, 'a+', encoding='UTF8', newline='') as f:  # a+ ------> append
                writer = csv.writer(f)
                writer.writerows(DATA30_hum)
        elif a == 31:
            with open(temp_file, 'a+', encoding='UTF8', newline='') as f:  # a+ ------> append
                writer = csv.writer(f)
                writer.writerows(DATA31)
            with open(hum_file, 'a+', encoding='UTF8', newline='') as f:  # a+ ------> append
                writer = csv.writer(f)
                writer.writerows(DATA31_hum)
        elif a == 32:
            with open(temp_file, 'a+', encoding='UTF8', newline='') as f:  # a+ ------> append
                writer = csv.writer(f)
                writer.writerows(DATA32)
            with open(hum_file, 'a+', encoding='UTF8', newline='') as f:  # a+ ------> append
                writer = csv.writer(f)
                writer.writerows(DATA32_hum)

        elif a == 33:
            with open(temp_file, 'a+', encoding='UTF8', newline='') as f:  # a+ ------> append
                writer = csv.writer(f)
                writer.writerows(DATA33)
            with open(hum_file, 'a+', encoding='UTF8', newline='') as f:  # a+ ------> append
                writer = csv.writer(f)
                writer.writerows(DATA33_hum)
        elif a == 34:
            with open(temp_file, 'a+', encoding='UTF8', newline='') as f:  # a+ ------> append
                writer = csv.writer(f)
                writer.writerows(DATA34)
            with open(hum_file, 'a+', encoding='UTF8', newline='') as f:  # a+ ------> append
                writer = csv.writer(f)
                writer.writerows(DATA34_hum)
        elif a == 35:
            with open(temp_file, 'a+', encoding='UTF8', newline='') as f:  # a+ ------> append
                writer = csv.writer(f)
                writer.writerows(DATA35)
            with open(hum_file, 'a+', encoding='UTF8', newline='') as f:  # a+ ------> append
                writer = csv.writer(f)
                writer.writerows(DATA35_hum)

        elif a == 36:
            with open(temp_file, 'a+', encoding='UTF8', newline='') as f:  # a+ ------> append
                writer = csv.writer(f)
                writer.writerows(DATA36)
            with open(hum_file, 'a+', encoding='UTF8', newline='') as f:  # a+ ------> append
                writer = csv.writer(f)
                writer.writerows(DATA36_hum)
        elif a == 37:
            with open(temp_file, 'a+', encoding='UTF8', newline='') as f:  # a+ ------> append
                writer = csv.writer(f)
                writer.writerows(DATA37)
            with open(hum_file, 'a+', encoding='UTF8', newline='') as f:  # a+ ------> append
                writer = csv.writer(f)
                writer.writerows(DATA37_hum)
        elif a == 38:
            with open(temp_file, 'a+', encoding='UTF8', newline='') as f:  # a+ ------> append
                writer = csv.writer(f)
                writer.writerows(DATA38)
            with open(hum_file, 'a+', encoding='UTF8', newline='') as f:  # a+ ------> append
                writer = csv.writer(f)
                writer.writerows(DATA38_hum)


        else:
            print("hi")

    def read(temp_file, hum_file, title, size):

        print(size)

        # display last 10 row in sheet
        df = pd.read_csv(temp_file).tail(size)

        df1 = pd.read_csv(hum_file).tail(size)
        # vertical spacing is space between 2 subplots ---> ,vertical_spacing=0.3
        fig = make_subplots(rows=2, cols=1, vertical_spacing=0.4)
        fig.add_trace(go.Scatter(x=df['Time'], y=df['Temperature'], name='Temperature', mode='lines'), row=1, col=1)
        fig.add_trace(go.Scatter(x=df1['Time'], y=df1['Humditiy'], name='humditiy', mode='lines'), row=2, col=1)

        fig.update_layout(title={
            'text': '<b>' + title + '</b>',
            'y': 0.9,
            'x': 0.5,
            'xanchor': 'right',
            'yanchor': 'middle',
        },
            title_font_color="rgb(0, 170, 255)",

            plot_bgcolor='rgb(230, 230,230)',

            images=[dict(
                source=Image.open("20.png"),
                xref="paper",
                yref="paper",

                x=.5,
                y=.44,
                xanchor="center",
                yanchor="middle",
                sizex=1.3,
                sizey=1.5,
                sizing="stretch",
                layer="below")],
            font=dict(

                size=14,
                color="black"
            ),

            showlegend=True)

        return fig

    def yarb4(self):
        while 1 == 1:
            print(datetime.datetime.now())
            if self.n == 0 and self.z == 0:
                no.noha("C:/Users/noha.omar/Desktop/Govee1/yarb1_temp.csv",
                        "C:/Users/noha.omar/Desktop/Govee1/yarb1_hum.csv", 13)
                no.noha("C:/Users/noha.omar/Desktop/Govee1/yarb2_temp.csv",
                        "C:/Users/noha.omar/Desktop/Govee1/yarb2_hum.csv", 12)
                no.noha("C:/Users/noha.omar/Desktop/Govee1/yarb3_temp.csv",
                        "C:/Users/noha.omar/Desktop/Govee1/yarb3_hum.csv", 11)
                no.noha("C:/Users/noha.omar/Desktop/Govee1/yarb4_temp.csv",
                        "C:/Users/noha.omar/Desktop/Govee1/yarb4_hum.csv", 10)
                no.noha("C:/Users/noha.omar/Desktop/Govee1/yarb5_temp.csv",
                        "C:/Users/noha.omar/Desktop/Govee1/yarb5_hum.csv", 9)
                no.noha("C:/Users/noha.omar/Desktop/Govee1/yarb6_temp.csv",
                        "C:/Users/noha.omar/Desktop/Govee1/yarb6_hum.csv", 8)
                print("1")
                no.noha("C:/Users/noha.omar/Desktop/Govee1/yarb7_temp.csv",
                        "C:/Users/noha.omar/Desktop/Govee1/yarb7_hum.csv", 7)
                no.noha("C:/Users/noha.omar/Desktop/Govee1/yarb8_temp.csv",
                        "C:/Users/noha.omar/Desktop/Govee1/yarb8_hum.csv", 6)
                no.noha("C:/Users/noha.omar/Desktop/Govee1/yarb9_temp.csv",
                        "C:/Users/noha.omar/Desktop/Govee1/yarb9_hum.csv", 14)
                no.noha("C:/Users/noha.omar/Desktop/Govee1/yarb10_temp.csv",
                        "C:/Users/noha.omar/Desktop/Govee1/yarb10_hum.csv", 13)
                no.noha("C:/Users/noha.omar/Desktop/Govee1/yarb11_temp.csv",
                        "C:/Users/noha.omar/Desktop/Govee1/yarb11_hum.csv", 12)
                print("2")
                no.noha("C:/Users/noha.omar/Desktop/Govee1/yarb12_temp.csv",
                        "C:/Users/noha.omar/Desktop/Govee1/yarb12_hum.csv", 11)
                # no.noha("C:/Users/noha.omar/Desktop/Govee1/yarb13_temp.csv",
                #         "C:/Users/noha.omar/Desktop/Govee1/yarb13_hum.csv", 10)
                no.noha("C:/Users/noha.omar/Desktop/Govee1/yarb14_temp.csv",
                        "C:/Users/noha.omar/Desktop/Govee1/yarb14_hum.csv", 9)
                no.noha("C:/Users/noha.omar/Desktop/Govee1/yarb15_temp.csv",
                        "C:/Users/noha.omar/Desktop/Govee1/yarb15_hum.csv", 8)

                no.noha("C:/Users/noha.omar/Desktop/Govee1/yarb16_temp.csv",
                        "C:/Users/noha.omar/Desktop/Govee1/yarb16_hum.csv", 7)
                print("3")
                no.noha("C:/Users/noha.omar/Desktop/Govee1/yarb20_temp.csv",
                        "C:/Users/noha.omar/Desktop/Govee1/yarb20_hum.csv", 6)
                no.noha("C:/Users/noha.omar/Desktop/Govee1/yarb21_temp.csv",
                        "C:/Users/noha.omar/Desktop/Govee1/yarb21_hum.csv", 14)
                no.noha("C:/Users/noha.omar/Desktop/Govee1/yarb22_temp.csv",
                        "C:/Users/noha.omar/Desktop/Govee1/yarb22_hum.csv", 14)
                no.noha("C:/Users/noha.omar/Desktop/Govee1/yarb23_temp.csv",
                        "C:/Users/noha.omar/Desktop/Govee1/yarb23_hum.csv", 13)
                no.noha("C:/Users/noha.omar/Desktop/Govee1/yarb24_temp.csv",
                        "C:/Users/noha.omar/Desktop/Govee1/yarb24_hum.csv", 12)
                print("4")
                no.noha("C:/Users/noha.omar/Desktop/Govee1/yarb25_temp.csv",
                        "C:/Users/noha.omar/Desktop/Govee1/yarb25_hum.csv", 11)
                no.noha("C:/Users/noha.omar/Desktop/Govee1/yarb26_temp.csv",
                        "C:/Users/noha.omar/Desktop/Govee1/yarb26_hum.csv", 10)
                no.noha("C:/Users/noha.omar/Desktop/Govee1/yarb27_temp.csv",
                        "C:/Users/noha.omar/Desktop/Govee1/yarb27_hum.csv", 9)
                no.noha("C:/Users/noha.omar/Desktop/Govee1/yarb28_temp.csv",
                        "C:/Users/noha.omar/Desktop/Govee1/yarb28_hum.csv", 8)
                no.noha("C:/Users/noha.omar/Desktop/Govee1/yarb29_temp.csv",
                        "C:/Users/noha.omar/Desktop/Govee1/yarb29_hum.csv", 7)
                print("6")
                no.noha("C:/Users/noha.omar/Desktop/Govee1/yarb30_temp.csv",
                        "C:/Users/noha.omar/Desktop/Govee1/yarb30_hum.csv", 6)
                no.noha("C:/Users/noha.omar/Desktop/Govee1/yarb31_temp.csv",
                        "C:/Users/noha.omar/Desktop/Govee1/yarb31_hum.csv", 14)
                # no.noha("C:/Users/noha.omar/Desktop/Govee1/yarb32_temp.csv",
                #         "C:/Users/noha.omar/Desktop/Govee1/yarb32_hum.csv", 1)
                no.noha("C:/Users/noha.omar/Desktop/Govee1/yarb33_temp.csv",
                        "C:/Users/noha.omar/Desktop/Govee1/yarb33_hum.csv", 3)
                no.noha("C:/Users/noha.omar/Desktop/Govee1/yarb34_temp.csv",
                        "C:/Users/noha.omar/Desktop/Govee1/yarb34_hum.csv", 5)
                no.noha("C:/Users/noha.omar/Desktop/Govee1/yarb35_temp.csv",
                        "C:/Users/noha.omar/Desktop/Govee1/yarb35_hum.csv", 2)
                no.noha("C:/Users/noha.omar/Desktop/Govee1/yarb36_temp.csv",
                        "C:/Users/noha.omar/Desktop/Govee1/yarb36_hum.csv", 4)
                # no.noha("C:/Users/noha.omar/Desktop/Govee1/yarb37_temp.csv",
                #         "C:/Users/noha.omar/Desktop/Govee1/yarb37_hum.csv", 4)
                no.noha("C:/Users/noha.omar/Desktop/Govee1/yarb38_temp.csv",
                        "C:/Users/noha.omar/Desktop/Govee1/yarb38_hum.csv", 3)
                # no.noha("C:/Users/noha.omar/Desktop/Govee1/yarb39_temp.csv",
                #         "C:/Users/noha.omar/Desktop/Govee1/yarb39_hum.csv", 1)
                no.noha("C:/Users/noha.omar/Desktop/Govee1/yarb40_temp.csv",
                        "C:/Users/noha.omar/Desktop/Govee1/yarb40_hum.csv", 5)
                no.noha("C:/Users/noha.omar/Desktop/Govee1/yarb41_temp.csv",
                        "C:/Users/noha.omar/Desktop/Govee1/yarb41_hum.csv", 1)
                no.noha("C:/Users/noha.omar/Desktop/Govee1/yarb42_temp.csv",
                        "C:/Users/noha.omar/Desktop/Govee1/yarb42_hum.csv", 3)
                no.noha("C:/Users/noha.omar/Desktop/Govee1/yarb43_temp.csv",
                        "C:/Users/noha.omar/Desktop/Govee1/yarb43_hum.csv", 2)
                no.noha("C:/Users/noha.omar/Desktop/Govee1/yarb44_temp.csv",
                        "C:/Users/noha.omar/Desktop/Govee1/yarb44_hum.csv", 4)
                no.noha("C:/Users/noha.omar/Desktop/Govee1/yarb45_temp.csv",
                        "C:/Users/noha.omar/Desktop/Govee1/yarb45_hum.csv", 5)
                no.noha("C:/Users/noha.omar/Desktop/Govee1/yarb46_temp.csv",
                        "C:/Users/noha.omar/Desktop/Govee1/yarb46_hum.csv", 1)
                no.noha("C:/Users/noha.omar/Desktop/Govee1/yarb47_temp.csv",
                        "C:/Users/noha.omar/Desktop/Govee1/yarb47_hum.csv", 3)
                no.noha("C:/Users/noha.omar/Desktop/Govee1/yarb48_temp.csv",
                        "C:/Users/noha.omar/Desktop/Govee1/yarb48_hum.csv", 2)
                no.noha("C:/Users/noha.omar/Desktop/Govee1/yarb49_temp.csv",
                        "C:/Users/noha.omar/Desktop/Govee1/yarb49_hum.csv", 4)
                no.noha("C:/Users/noha.omar/Desktop/Govee1/yarb50_temp.csv",
                        "C:/Users/noha.omar/Desktop/Govee1/yarb50_hum.csv", 2)
                no.noha("C:/Users/noha.omar/Desktop/Govee1/yarb51_temp.csv",
                        "C:/Users/noha.omar/Desktop/Govee1/yarb51_hum.csv", 5)
                no.noha("C:/Users/noha.omar/Desktop/Govee1/yarb52_temp.csv",
                        "C:/Users/noha.omar/Desktop/Govee1/yarb52_hum.csv", 1)
                no.noha("C:/Users/noha.omar/Desktop/Govee1/yarb53_temp.csv",
                        "C:/Users/noha.omar/Desktop/Govee1/yarb53_hum.csv", 2)
                no.noha("C:/Users/noha.omar/Desktop/Govee1/yarb54_temp.csv",
                        "C:/Users/noha.omar/Desktop/Govee1/yarb54_hum.csv", 4)
                no.noha("C:/Users/noha.omar/Desktop/Govee1/yarb55_temp.csv",
                        "C:/Users/noha.omar/Desktop/Govee1/yarb55_hum.csv", 3)
                no.noha("C:/Users/noha.omar/Desktop/Govee1/yarb56_temp.csv",
                        "C:/Users/noha.omar/Desktop/Govee1/yarb56_hum.csv", 1)
                no.noha("C:/Users/noha.omar/Desktop/Govee1/yarb57_temp.csv",
                        "C:/Users/noha.omar/Desktop/Govee1/yarb57_hum.csv", 13)
                no.noha("C:/Users/noha.omar/Desktop/Govee1/yarb58_temp.csv",
                        "C:/Users/noha.omar/Desktop/Govee1/yarb58_hum.csv", 12)
                print("noha58")
                no.noha("C:/Users/noha.omar/Desktop/Govee1/yarb59_temp.csv",
                        "C:/Users/noha.omar/Desktop/Govee1/yarb59_hum.csv", 11)
                no.noha("C:/Users/noha.omar/Desktop/Govee1/yarb60_temp.csv",
                        "C:/Users/noha.omar/Desktop/Govee1/yarb60_hum.csv", 10)
                no.noha("C:/Users/noha.omar/Desktop/Govee1/yarb61_temp.csv",
                        "C:/Users/noha.omar/Desktop/Govee1/yarb61_hum.csv", 9)
                no.noha("C:/Users/noha.omar/Desktop/Govee1/yarb62_temp.csv",
                        "C:/Users/noha.omar/Desktop/Govee1/yarb62_hum.csv", 8)
                no.noha("C:/Users/noha.omar/Desktop/Govee1/yarb63_temp.csv",
                        "C:/Users/noha.omar/Desktop/Govee1/yarb63_hum.csv", 7)
                no.noha("C:/Users/noha.omar/Desktop/Govee1/yarb64_temp.csv",
                        "C:/Users/noha.omar/Desktop/Govee1/yarb64_hum.csv", 6)
                print("65")
                no.noha("C:/Users/noha.omar/Desktop/Govee1/yarb65_temp.csv",
                        "C:/Users/noha.omar/Desktop/Govee1/yarb65_hum.csv", 14)
                no.noha("C:/Users/noha.omar/Desktop/Govee1/yarb66_temp.csv",
                        "C:/Users/noha.omar/Desktop/Govee1/yarb66_hum.csv", 13)
                no.noha("C:/Users/noha.omar/Desktop/Govee1/yarb67_temp.csv",
                        "C:/Users/noha.omar/Desktop/Govee1/yarb67_hum.csv", 12)
                # no.noha("C:/Users/noha.omar/Desktop/Govee1/yarb68_temp.csv",
                #         "C:/Users/noha.omar/Desktop/Govee1/yarb68_hum.csv", 11)
                no.noha("C:/Users/noha.omar/Desktop/Govee1/yarb69_temp.csv",
                        "C:/Users/noha.omar/Desktop/Govee1/yarb69_hum.csv", 10)
                no.noha("C:/Users/noha.omar/Desktop/Govee1/yarb70_temp.csv",
                        "C:/Users/noha.omar/Desktop/Govee1/yarb70_hum.csv", 9)
                no.noha("C:/Users/noha.omar/Desktop/Govee1/yarb71_temp.csv",
                        "C:/Users/noha.omar/Desktop/Govee1/yarb71_hum.csv", 17)
                no.noha("C:/Users/noha.omar/Desktop/Govee1/yarb72_temp.csv",
                        "C:/Users/noha.omar/Desktop/Govee1/yarb72_hum.csv", 18)
                no.noha("C:/Users/noha.omar/Desktop/Govee1/yarb73_temp.csv",
                        "C:/Users/noha.omar/Desktop/Govee1/yarb73_hum.csv", 8)
                no.noha("C:/Users/noha.omar/Desktop/Govee1/yarb74_temp.csv",
                        "C:/Users/noha.omar/Desktop/Govee1/yarb74_hum.csv", 7)
                no.noha("C:/Users/noha.omar/Desktop/Govee1/yarb75_temp.csv",
                        "C:/Users/noha.omar/Desktop/Govee1/yarb75_hum.csv", 31)
                no.noha("C:/Users/noha.omar/Desktop/Govee1/yarb76_temp.csv",
                        "C:/Users/noha.omar/Desktop/Govee1/yarb76_hum.csv", 26)
                no.noha("C:/Users/noha.omar/Desktop/Govee1/yarb77_temp.csv",
                        "C:/Users/noha.omar/Desktop/Govee1/yarb77_hum.csv", 25)
                no.noha("C:/Users/noha.omar/Desktop/Govee1/yarb78_temp.csv",
                        "C:/Users/noha.omar/Desktop/Govee1/yarb78_hum.csv", 29)
                no.noha("C:/Users/noha.omar/Desktop/Govee1/yarb79_temp.csv",
                        "C:/Users/noha.omar/Desktop/Govee1/yarb79_hum.csv", 27)
                no.noha("C:/Users/noha.omar/Desktop/Govee1/yarb80_temp.csv",
                        "C:/Users/noha.omar/Desktop/Govee1/yarb80_hum.csv", 2)
                no.noha("C:/Users/noha.omar/Desktop/Govee1/yarb81_temp.csv",
                        "C:/Users/noha.omar/Desktop/Govee1/yarb81_hum.csv", 1)
                no.noha("C:/Users/noha.omar/Desktop/Govee1/yarb82_temp.csv",
                        "C:/Users/noha.omar/Desktop/Govee1/yarb82_hum.csv", 4)
                no.noha("C:/Users/noha.omar/Desktop/Govee1/yarb83_temp.csv",
                        "C:/Users/noha.omar/Desktop/Govee1/yarb83_hum.csv", 1)
                no.noha("C:/Users/noha.omar/Desktop/Govee1/yarb84_temp.csv",
                        "C:/Users/noha.omar/Desktop/Govee1/yarb84_hum.csv", 24)
                no.noha("C:/Users/noha.omar/Desktop/Govee1/yarb85_temp.csv",
                        "C:/Users/noha.omar/Desktop/Govee1/yarb85_hum.csv", 18)
                no.noha("C:/Users/noha.omar/Desktop/Govee1/yarb86_temp.csv",
                        "C:/Users/noha.omar/Desktop/Govee1/yarb86_hum.csv", 13)
                no.noha("C:/Users/noha.omar/Desktop/Govee1/yarb87_temp.csv",
                        "C:/Users/noha.omar/Desktop/Govee1/yarb87_hum.csv", 32)
                no.noha("C:/Users/noha.omar/Desktop/Govee1/yarb88_temp.csv",
                        "C:/Users/noha.omar/Desktop/Govee1/yarb88_hum.csv", 33)
                no.noha("C:/Users/noha.omar/Desktop/Govee1/yarb89_temp.csv",
                        "C:/Users/noha.omar/Desktop/Govee1/yarb89_hum.csv", 34)
                no.noha("C:/Users/noha.omar/Desktop/Govee1/yarb90_temp.csv",
                        "C:/Users/noha.omar/Desktop/Govee1/yarb90_hum.csv", 35)
                no.noha("C:/Users/noha.omar/Desktop/Govee1/yarb91_temp.csv",
                        "C:/Users/noha.omar/Desktop/Govee1/yarb91_hum.csv", 28)
                no.noha("C:/Users/noha.omar/Desktop/Govee1/yarb93_temp.csv",
                        "C:/Users/noha.omar/Desktop/Govee1/yarb93_hum.csv", 3)
                no.noha("C:/Users/noha.omar/Desktop/Govee1/yarb94_temp.csv",
                        "C:/Users/noha.omar/Desktop/Govee1/yarb94_hum.csv", 23)
                no.noha("C:/Users/noha.omar/Desktop/Govee1/yarb95_temp.csv",
                        "C:/Users/noha.omar/Desktop/Govee1/yarb95_hum.csv", 30)
                no.noha("C:/Users/noha.omar/Desktop/Govee1/yarb96_temp.csv",
                        "C:/Users/noha.omar/Desktop/Govee1/yarb96_hum.csv", 36)
                no.noha("C:/Users/noha.omar/Desktop/Govee1/yarb97_temp.csv",
                        "C:/Users/noha.omar/Desktop/Govee1/yarb97_hum.csv", 37)
                no.noha("C:/Users/noha.omar/Desktop/Govee1/yarb98_temp.csv",
                        "C:/Users/noha.omar/Desktop/Govee1/yarb98_hum.csv", 38)

                time.sleep(900);

                self.n = 0
                self.z = 0

    def yarb5(self):
        print(datetime.datetime.now())
        if self.n == 1 and self.z == 1:
            sd = no.read("C:/Users/noha.omar/Desktop/Govee1/yarb1_temp.csv",
                         "C:/Users/noha.omar/Desktop/Govee1/yarb1_hum.csv", "Seive", 96)
            sd.write_html('Device- 1.html', auto_open=True)
        elif self.n == 2 and self.z == 1:
            sd = no.read("C:/Users/noha.omar/Desktop/Govee1/yarb2_temp.csv",
                         "C:/Users/noha.omar/Desktop/Govee1/yarb2_hum.csv", "V Shape", 96)
            sd.write_html('Device- 2.html', auto_open=True)

        elif self.n == 3 and self.z == 1:
            sd = no.read("C:/Users/noha.omar/Desktop/Govee1/yarb3_temp.csv",
                         "C:/Users/noha.omar/Desktop/Govee1/yarb3_hum.csv", "Small Coating", 96)
            sd.write_html('Device- 3.html', auto_open=True)
        elif self.n == 4 and self.z == 1:
            sd = no.read("C:/Users/noha.omar/Desktop/Govee1/yarb4_temp.csv",
                         "C:/Users/noha.omar/Desktop/Govee1/yarb4_hum.csv", "Holding Room", 96)
            sd.write_html('Device- 4.html', auto_open=True)

        elif self.n == 5 and self.z == 1:
            sd = no.read("C:/Users/noha.omar/Desktop/Govee1/yarb5_temp.csv",
                         "C:/Users/noha.omar/Desktop/Govee1/yarb5_hum.csv", "Coating Gansons(Room2)", 96)
            sd.write_html('Device- 5.html', auto_open=True)

        elif self.n == 6 and self.z == 1:
            sd = no.read("C:/Users/noha.omar/Desktop/Govee1/yarb6_temp.csv",
                         "C:/Users/noha.omar/Desktop/Govee1/yarb6_hum.csv", "Sachet Filling2", 96)
            sd.write_html('Device- 6.html', auto_open=True)
        elif self.n == 7 and self.z == 1:
            sd = no.read("C:/Users/noha.omar/Desktop/Govee1/yarb7_temp.csv",
                         "C:/Users/noha.omar/Desktop/Govee1/yarb7_hum.csv", "Pilot(R&D Granulation)", 96)
            sd.write_html('Device- 7.html', auto_open=True)
        elif self.n == 8 and self.z == 1:
            sd = no.read("C:/Users/noha.omar/Desktop/Govee1/yarb8_temp.csv",
                         "C:/Users/noha.omar/Desktop/Govee1/yarb8_hum.csv", "R&D Blinding", 96)
            sd.write_html('Device- 8.html', auto_open=True)
        elif self.n == 9 and self.z == 1:
            sd = no.read("C:/Users/noha.omar/Desktop/Govee1/yarb9_temp.csv",
                         "C:/Users/noha.omar/Desktop/Govee1/yarb9_hum.csv", "R&D Compression", 96)
            sd.write_html('Device- 9.html', auto_open=True)
        elif self.n == 10 and self.z == 1:
            sd = no.read("C:/Users/noha.omar/Desktop/Govee1/yarb10_temp.csv",
                         "C:/Users/noha.omar/Desktop/Govee1/yarb10_hum.csv", "Holding Room (028P1)(Middle)", 96)
            sd.write_html('Device- 10.html', auto_open=True)

        elif self.n == 11 and self.z == 1:
            sd = no.read("C:/Users/noha.omar/Desktop/Govee1/yarb11_temp.csv",
                         "C:/Users/noha.omar/Desktop/Govee1/yarb11_hum.csv", "Capsule FillinG(Old)", 96)
            sd.write_html('Device- 11.html', auto_open=True)
        elif self.n == 12 and self.z == 1:
            sd = no.read("C:/Users/noha.omar/Desktop/Govee1/yarb12_temp.csv",
                         "C:/Users/noha.omar/Desktop/Govee1/yarb12_hum.csv", "Compresstion Room1", 96)
            sd.write_html('Device- 12.html', auto_open=True)
        elif self.n == 13 and self.z == 1:
            sd = no.read("C:/Users/noha.omar/Desktop/Govee1/yarb13_temp.csv",
                         "C:/Users/noha.omar/Desktop/Govee1/yarb13_hum.csv", "Granulation", 96)
            sd.write_html('Device- 13.html', auto_open=True)

        elif self.n == 14 and self.z == 1:
            sd = no.read("C:/Users/noha.omar/Desktop/Govee1/yarb14_temp.csv",
                         "C:/Users/noha.omar/Desktop/Govee1/yarb14_hum.csv", "Bin Blender", 96)
            sd.write_html('Device- 14.html', auto_open=True)

        elif self.n == 15 and self.z == 1:
            sd = no.read("C:/Users/noha.omar/Desktop/Govee1/yarb15_temp.csv",
                         "C:/Users/noha.omar/Desktop/Govee1/yarb15_hum.csv", "Compresstion Room2", 96)
            sd.write_html('Device- 15.html', auto_open=True)
        elif self.n == 16 and self.z == 1:
            sd = no.read("C:/Users/noha.omar/Desktop/Govee1/yarb16_temp.csv",
                         "C:/Users/noha.omar/Desktop/Govee1/yarb16_hum.csv", "Granulation", 96)
            sd.write_html('Device- 16.html', auto_open=True)
        elif self.n == 20 and self.z == 1:
            sd = no.read("C:/Users/noha.omar/Desktop/Govee1/yarb20_temp.csv",
                         "C:/Users/noha.omar/Desktop/Govee1/yarb20_hum.csv", "Depaking Room For Solid", 96)
            sd.write_html('Device- 20.html', auto_open=True)
        elif self.n == 21 and self.z == 1:
            sd = no.read("C:/Users/noha.omar/Desktop/Govee1/yarb21_temp.csv",
                         "C:/Users/noha.omar/Desktop/Govee1/yarb21_hum.csv", "Bottle Clean For Dry Syrup", 96)
            sd.write_html('Device- 21.html', auto_open=True)
        elif self.n == 22 and self.z == 1:
            sd = no.read("C:/Users/noha.omar/Desktop/Govee1/yarb22_temp.csv",
                         "C:/Users/noha.omar/Desktop/Govee1/yarb22_hum.csv", " Dry Syrup Filling", 96)
            sd.write_html('Device- 22.html', auto_open=True)
        elif self.n == 23 and self.z == 1:
            sd = no.read("C:/Users/noha.omar/Desktop/Govee1/yarb23_temp.csv",
                         "C:/Users/noha.omar/Desktop/Govee1/yarb23_hum.csv", "Sachet FillinG(Old)", 96)
            sd.write_html('Device- 23.html', auto_open=True)
        elif self.n == 24 and self.z == 1:
            sd = no.read("C:/Users/noha.omar/Desktop/Govee1/yarb24_temp.csv",
                         "C:/Users/noha.omar/Desktop/Govee1/yarb24_hum.csv", "Coating Solution Prep ", 96)
            sd.write_html('Device- 24.html', auto_open=True)

        elif self.n == 25 and self.z == 1:
            sd = no.read("C:/Users/noha.omar/Desktop/Govee1/yarb25_temp.csv",
                         "C:/Users/noha.omar/Desktop/Govee1/yarb25_hum.csv", "Capsule Filling 2 ", 96)
            sd.write_html('Device- 25.html', auto_open=True)
        elif self.n == 26 and self.z == 1:
            sd = no.read("C:/Users/noha.omar/Desktop/Govee1/yarb26_temp.csv",
                         "C:/Users/noha.omar/Desktop/Govee1/yarb26_hum.csv", "Coating Room 1(Old) ", 96)
            sd.write_html('Device- 26.html', auto_open=True)
        elif self.n == 27 and self.z == 1:
            sd = no.read("C:/Users/noha.omar/Desktop/Govee1/yarb27_temp.csv",
                         "C:/Users/noha.omar/Desktop/Govee1/yarb27_hum.csv", "Corridor Against  sacchet Filling ", 96)
            sd.write_html('Device- 27.html', auto_open=True)

        elif self.n == 28 and self.z == 1:
            sd = no.read("C:/Users/noha.omar/Desktop/Govee1/yarb28_temp.csv",
                         "C:/Users/noha.omar/Desktop/Govee1/yarb28_hum.csv", "Corridor Against V Shape ", 96)
            sd.write_html('Fifth_device.html', auto_open=True)

        elif self.n == 29 and self.z == 1:
            sd = no.read("C:/Users/noha.omar/Desktop/Govee1/yarb29_temp.csv",
                         "C:/Users/noha.omar/Desktop/Govee1/yarb29_hum.csv", "Stage Out (Solid area)", 96)
            sd.write_html('Device- 29.html', auto_open=True)
        elif self.n == 30 and self.z == 1:
            sd = no.read("C:/Users/noha.omar/Desktop/Govee1/yarb30_temp.csv",
                         "C:/Users/noha.omar/Desktop/Govee1/yarb30_hum.csv", "Corridor Against IPC ", 96)
            sd.write_html('Device- 30.html', auto_open=True)

        elif self.n == 31 and self.z == 1:
            sd = no.read("C:/Users/noha.omar/Desktop/Govee1/yarb31_temp.csv",
                         "C:/Users/noha.omar/Desktop/Govee1/yarb31_hum.csv", "MAl (Solid area)", 96)
            sd.write_html('Device- 31.html', auto_open=True)
        elif self.n == 32 and self.z == 1:
            sd = no.read("C:/Users/noha.omar/Desktop/Govee1/yarb32_temp.csv",
                         "C:/Users/noha.omar/Desktop/Govee1/yarb32_hum.csv", "Cleaning Room for Liquid bottle1(Old)", 96)
            sd.write_html('Device- 32.html', auto_open=True)
        elif self.n == 33 and self.z == 1:
            sd = no.read("C:/Users/noha.omar/Desktop/Govee1/yarb33_temp.csv",
                         "C:/Users/noha.omar/Desktop/Govee1/yarb33_hum.csv", "Filling Room for Liquid 1(Old)", 96)
            sd.write_html('Device- 33.html', auto_open=True)
        elif self.n == 34 and self.z == 1:
            sd = no.read("C:/Users/noha.omar/Desktop/Govee1/yarb34_temp.csv",
                         "C:/Users/noha.omar/Desktop/Govee1/yarb34_hum.csv", "Cleaning Room for Liquid bottle2(new)", 96)
            sd.write_html('Device- 34.html', auto_open=True)
        elif self.n == 35 and self.z == 1:
            sd = no.read("C:/Users/noha.omar/Desktop/Govee1/yarb35_temp.csv",
                         "C:/Users/noha.omar/Desktop/Govee1/yarb35_hum.csv", "Filling Room for Liquid 2(new)", 96)
            sd.write_html('Device- 35.html', auto_open=True)

        elif self.n == 36 and self.z == 1:
            sd = no.read("C:/Users/noha.omar/Desktop/Govee1/yarb36_temp.csv",
                         "C:/Users/noha.omar/Desktop/Govee1/yarb36_hum.csv", "MAL 1 Inner Part", 96)
            sd.write_html('Device- 36.html', auto_open=True)
        elif self.n == 37 and self.z == 1:
            sd = no.read("C:/Users/noha.omar/Desktop/Govee1/yarb37_temp.csv",
                         "C:/Users/noha.omar/Desktop/Govee1/yarb37_hum.csv", "MAL 1 Outer Part", 96)
            sd.write_html('Device- 37.html', auto_open=True)
        elif self.n == 38 and self.z == 1:
            sd = no.read("C:/Users/noha.omar/Desktop/Govee1/yarb38_temp.csv",
                         "C:/Users/noha.omar/Desktop/Govee1/yarb38_hum.csv", "MAL 2 Inner Part", 96)
            sd.write_html('Device- 38.html', auto_open=True)

        elif self.n == 39 and self.z == 1:
            sd = no.read("C:/Users/noha.omar/Desktop/Govee1/yarb39_temp.csv",
                         "C:/Users/noha.omar/Desktop/Govee1/yarb39_hum.csv", "MAL 2 Outer Part", 96)
            sd.write_html('Device- 39.html', auto_open=True)

        elif self.n == 40 and self.z == 1:
            sd = no.read("C:/Users/noha.omar/Desktop/Govee1/yarb40_temp.csv",
                         "C:/Users/noha.omar/Desktop/Govee1/yarb40_hum.csv", "Corridor Liquid First Floor", 96)
            sd.write_html('Device- 40.html', auto_open=True)

        elif self.n == 41 and self.z == 1:
            sd = no.read("C:/Users/noha.omar/Desktop/Govee1/yarb41_temp.csv",
                         "C:/Users/noha.omar/Desktop/Govee1/yarb41_hum.csv", "SS2 Packaging Syrup", 96)
            sd.write_html('Device- 41.html', auto_open=True)

        elif self.n == 42 and self.z == 1:
            sd = no.read("C:/Users/noha.omar/Desktop/Govee1/yarb42_temp.csv",
                         "C:/Users/noha.omar/Desktop/Govee1/yarb42_hum.csv", "Syrup Packaging EMA Safe", 96)
            sd.write_html('Device- 42.html', auto_open=True)
        elif self.n == 43 and self.z == 1:
            sd = no.read("C:/Users/noha.omar/Desktop/Govee1/yarb43_temp.csv",
                         "C:/Users/noha.omar/Desktop/Govee1/yarb43_hum.csv", "Semisolid Filling 3", 96)
            sd.write_html('Device- 43.html', auto_open=True)
        elif self.n == 44 and self.z == 1:
            sd = no.read("C:/Users/noha.omar/Desktop/Govee1/yarb44_temp.csv",
                         "C:/Users/noha.omar/Desktop/Govee1/yarb44_hum.csv", "Sk (Liq.Prep 2)", 96)
            sd.write_html('Device- 44.html', auto_open=True)
        elif self.n == 45 and self.z == 1:
            sd = no.read("C:/Users/noha.omar/Desktop/Govee1/yarb45_temp.csv",
                         "C:/Users/noha.omar/Desktop/Govee1/yarb45_hum.csv", "Fryma Old (Cream Prep)", 96)
            sd.write_html('Device- 45.html', auto_open=True)
        elif self.n == 46 and self.z == 1:
            sd = no.read("C:/Users/noha.omar/Desktop/Govee1/yarb46_temp.csv",
                         "C:/Users/noha.omar/Desktop/Govee1/yarb46_hum.csv", "Fryma New (Semisolid Prep)", 96)
            sd.write_html('Device- 46.html', auto_open=True)
        elif self.n == 47 and self.z == 1:
            sd = no.read("C:/Users/noha.omar/Desktop/Govee1/yarb47_temp.csv",
                         "C:/Users/noha.omar/Desktop/Govee1/yarb47_hum.csv", "Liq . Prep 1(Old)", 96)
            sd.write_html('Device- 47.html', auto_open=True)

        elif self.n == 48 and self.z == 1:
            sd = no.read("C:/Users/noha.omar/Desktop/Govee1/yarb48_temp.csv",
                         "C:/Users/noha.omar/Desktop/Govee1/yarb48_hum.csv", "Axomatic New (Semisolid Filling 2)", 96)
            sd.write_html('Device- 48.html', auto_open=True)
        elif self.n == 49 and self.z == 1:
            sd = no.read("C:/Users/noha.omar/Desktop/Govee1/yarb49_temp.csv",
                         "C:/Users/noha.omar/Desktop/Govee1/yarb49_hum.csv", "Axomatic Old (Semisolid Filling 1)", 96)
            sd.write_html('Device- 49.html', auto_open=True)
        elif self.n == 50 and self.z == 1:
            sd = no.read("C:/Users/noha.omar/Desktop/Govee1/yarb50_temp.csv",
                         "C:/Users/noha.omar/Desktop/Govee1/yarb50_hum.csv", "Ext. Prep Room", 96)
            sd.write_html('Device- 50.html', auto_open=True)

        elif self.n == 51 and self.z == 1:
            sd = no.read("C:/Users/noha.omar/Desktop/Govee1/yarb51_temp.csv",
                         "C:/Users/noha.omar/Desktop/Govee1/yarb51_hum.csv", "Ext. Cleaning Line", 96)
            sd.write_html('Device- 51.html', auto_open=True)

        elif self.n == 52 and self.z == 1:
            sd = no.read("C:/Users/noha.omar/Desktop/Govee1/yarb52_temp.csv",
                         "C:/Users/noha.omar/Desktop/Govee1/yarb52_hum.csv", "Ext. Filling Line", 96)
            sd.write_html('Device- 52', auto_open=True)
        elif self.n == 53 and self.z == 1:
            sd = no.read("C:/Users/noha.omar/Desktop/Govee1/yarb53_temp.csv",
                         "C:/Users/noha.omar/Desktop/Govee1/yarb53_hum.csv", "Depaking Room for Liquid", 96)
            sd.write_html('Device- 53.html', auto_open=True)
        elif self.n == 54 and self.z == 1:
            sd = no.read("C:/Users/noha.omar/Desktop/Govee1/yarb54_temp.csv",
                         "C:/Users/noha.omar/Desktop/Govee1/yarb54_hum.csv", "Corridor in Liquid area(2nd Floor)", 96)
            sd.write_html('Device- 54.html', auto_open=True)

        elif self.n == 55 and self.z == 1:
            sd = no.read("C:/Users/noha.omar/Desktop/Govee1/yarb55_temp.csv",
                         "C:/Users/noha.omar/Desktop/Govee1/yarb55_hum.csv", "MAl Semisolid Inner Part", 96)
            sd.write_html('Device- 55.html', auto_open=True)

        elif self.n == 56 and self.z == 1:
            sd = no.read("C:/Users/noha.omar/Desktop/Govee1/yarb56_temp.csv",
                         "C:/Users/noha.omar/Desktop/Govee1/yarb56_hum.csv", "MAl Semisolid Outer Part", 96)
            sd.write_html('Device- 56.html', auto_open=True)
        elif self.n == 57 and self.z == 1:
            sd = no.read("C:/Users/noha.omar/Desktop/Govee1/yarb57_temp.csv",
                         "C:/Users/noha.omar/Desktop/Govee1/yarb57_hum.csv", "Partina (Blistering Room 1)", 96)
            sd.write_html('Device- 57.html', auto_open=True)
        elif self.n == 58 and self.z == 1:
            sd = no.read("C:/Users/noha.omar/Desktop/Govee1/yarb58_temp.csv",
                         "C:/Users/noha.omar/Desktop/Govee1/yarb58_hum.csv", "Tablet Counter Room", 96)
            sd.write_html('Device- 58.html', auto_open=True)
        elif self.n == 59 and self.z == 1:
            sd = no.read("C:/Users/noha.omar/Desktop/Govee1/yarb59_temp.csv",
                         "C:/Users/noha.omar/Desktop/Govee1/yarb59_hum.csv", "Pam New (Bilistering 3)", 96)
            sd.write_html('Device- 59.html', auto_open=True)

        elif self.n == 60 and self.z == 1:
            sd = no.read("C:/Users/noha.omar/Desktop/Govee1/yarb60_temp.csv",
                         "C:/Users/noha.omar/Desktop/Govee1/yarb60_hum.csv", "Pam Old (Bilistering 2)", 96)
            sd.write_html('Device- 60.html', auto_open=True)
        elif self.n == 61 and self.z == 1:
            sd = no.read("C:/Users/noha.omar/Desktop/Govee1/yarb61_temp.csv",
                         "C:/Users/noha.omar/Desktop/Govee1/yarb61_hum.csv", "MAL Bilistering ", 96)
            sd.write_html('Device- 61.html', auto_open=True)
        elif self.n == 62 and self.z == 1:
            sd = no.read("C:/Users/noha.omar/Desktop/Govee1/yarb62_temp.csv",
                         "C:/Users/noha.omar/Desktop/Govee1/yarb62_hum.csv", " Bilistering  Corridor", 96)
            sd.write_html('Device- 62.html', auto_open=True)

        elif self.n == 63 and self.z == 1:
            sd = no.read("C:/Users/noha.omar/Desktop/Govee1/yarb63_temp.csv",
                         "C:/Users/noha.omar/Desktop/Govee1/yarb63_hum.csv", " SS (Packaging Machine)", 96)
            sd.write_html('Device- 63.html', auto_open=True)

        elif self.n == 64 and self.z == 1:
            sd = no.read("C:/Users/noha.omar/Desktop/Govee1/yarb64_temp.csv",
                         "C:/Users/noha.omar/Desktop/Govee1/yarb64_hum.csv", " Packaging Blister", 96)
            sd.write_html('Device- 64.html', auto_open=True)
        elif self.n == 65 and self.z == 1:
            sd = no.read("C:/Users/noha.omar/Desktop/Govee1/yarb65_temp.csv",
                         "C:/Users/noha.omar/Desktop/Govee1/yarb65_hum.csv", " Pamphlet Area (Metronic Machine)", 96)
            sd.write_html('Device- 65.html', auto_open=True)
        elif self.n == 66 and self.z == 1:
            sd = no.read("C:/Users/noha.omar/Desktop/Govee1/yarb66_temp.csv",
                         "C:/Users/noha.omar/Desktop/Govee1/yarb66_hum.csv", " Holding Room Packaging Area", 96)
            sd.write_html('Device- 66.html', auto_open=True)

        elif self.n == 67 and self.z == 1:
            sd = no.read("C:/Users/noha.omar/Desktop/Govee1/yarb67_temp.csv",
                         "C:/Users/noha.omar/Desktop/Govee1/yarb67_hum.csv", " Weight Room 1", 96)
            sd.write_html('Device- 67.html', auto_open=True)

        elif self.n == 68 and self.z == 1:
            sd = no.read("C:/Users/noha.omar/Desktop/Govee1/yarb68_temp.csv",
                         "C:/Users/noha.omar/Desktop/Govee1/yarb68_hum.csv", " Weight Room 2", 96)
            sd.write_html('Device- 68.html', auto_open=True)

        elif self.n == 69 and self.z == 1:
            sd = no.read("C:/Users/noha.omar/Desktop/Govee1/yarb69_temp.csv",
                         "C:/Users/noha.omar/Desktop/Govee1/yarb69_hum.csv", " Weight Corridor", 96)
            sd.write_html('Device- 69.html', auto_open=True)

        elif self.n == 70 and self.z == 1:
            sd = no.read("C:/Users/noha.omar/Desktop/Govee1/yarb70_temp.csv",
                         "C:/Users/noha.omar/Desktop/Govee1/yarb70_hum.csv", "Sampling", 96)
            sd.write_html('Device- 70.html', auto_open=True)
        elif self.n == 71 and self.z == 1:
            sd = no.read("C:/Users/noha.omar/Desktop/Govee1/yarb71_temp.csv",
                         "C:/Users/noha.omar/Desktop/Govee1/yarb71_hum.csv", "QC Fridge", 96)
            sd.write_html('Device- 71.html', auto_open=True)
        elif self.n == 72 and self.z == 1:
            sd = no.read("C:/Users/noha.omar/Desktop/Govee1/yarb72_temp.csv",
                         "C:/Users/noha.omar/Desktop/Govee1/yarb72_hum.csv", "QC Freezer", 96)
            sd.write_html('Device- 72.html', auto_open=True)
        elif self.n == 73 and self.z == 1:
            sd = no.read("C:/Users/noha.omar/Desktop/Govee1/yarb70_temp.csv",
                         "C:/Users/noha.omar/Desktop/Govee1/yarb73_hum.csv", "Packaging (Pd Sticking Machine)", 96)
            sd.write_html('Device- 73.html', auto_open=True)
        elif self.n == 74 and self.z == 1:
            sd = no.read("C:/Users/noha.omar/Desktop/Govee1/yarb74_temp.csv",
                         "C:/Users/noha.omar/Desktop/Govee1/yarb74_hum.csv", "CIP (2nd Floor)", 96)
            sd.write_html('Device- 74.html', auto_open=True)
        elif self.n == 75 and self.z == 1:
            sd = no.read("C:/Users/noha.omar/Desktop/Govee1/yarb75_temp.csv",
                         "C:/Users/noha.omar/Desktop/Govee1/yarb75_hum.csv", "Cold Store", 96)
            sd.write_html('Device- 75.html', auto_open=True)
        elif self.n == 76 and self.z == 1:
            sd = no.read("C:/Users/noha.omar/Desktop/Govee1/yarb76_temp.csv",
                         "C:/Users/noha.omar/Desktop/Govee1/yarb76_hum.csv", "Small Stability", 96)
            sd.write_html('Device- 76.html', auto_open=True)
        elif self.n == 77 and self.z == 1:
            sd = no.read("C:/Users/noha.omar/Desktop/Govee1/yarb77_temp.csv",
                         "C:/Users/noha.omar/Desktop/Govee1/yarb77_hum.csv", "Large Stability", 96)
            sd.write_html('Device- 77.html', auto_open=True)
        elif self.n == 78 and self.z == 1:
            sd = no.read("C:/Users/noha.omar/Desktop/Govee1/yarb78_temp.csv",
                         "C:/Users/noha.omar/Desktop/Govee1/yarb78_hum.csv", "R&D LAB", 96)
            sd.write_html('Device- 78.html', auto_open=True)
        elif self.n == 79 and self.z == 1:
            sd = no.read("C:/Users/noha.omar/Desktop/Govee1/yarb79_temp.csv",
                         "C:/Users/noha.omar/Desktop/Govee1/yarb79_hum.csv", "R&D Fridge", 96)
            sd.write_html('Device- 79.html', auto_open=True)
        elif self.n == 80 and self.z == 1:
            sd = no.read("C:/Users/noha.omar/Desktop/Govee1/yarb80_temp.csv",
                         "C:/Users/noha.omar/Desktop/Govee1/yarb80_hum.csv", "QC", 96)
            sd.write_html('Device- 80.html', auto_open=True)
        elif self.n == 81 and self.z == 1:
            sd = no.read("C:/Users/noha.omar/Desktop/Govee1/yarb81_temp.csv",
                         "C:/Users/noha.omar/Desktop/Govee1/yarb81_hum.csv", "Cleaning room for liquid bottle 1(old)",
                         96)
            sd.write_html('Device- 81.html', auto_open=True)
        elif self.n == 82 and self.z == 1:
            sd = no.read("C:/Users/noha.omar/Desktop/Govee1/yarb82_temp.csv",
                         "C:/Users/noha.omar/Desktop/Govee1/yarb82_hum.csv", "MAL 1 OUTER PART", 96)
            sd.write_html('Device- 82.html', auto_open=True)
        elif self.n == 83 and self.z == 1:
            sd = no.read("C:/Users/noha.omar/Desktop/Govee1/yarb83_temp.csv",
                         "C:/Users/noha.omar/Desktop/Govee1/yarb83_hum.csv", "MAL 2 OUTER PART", 96)
            sd.write_html('Device- 83.html', auto_open=True)
        elif self.n == 84 and self.z == 1:
            sd = no.read("C:/Users/noha.omar/Desktop/Govee1/yarb84_temp.csv",
                         "C:/Users/noha.omar/Desktop/Govee1/yarb84_hum.csv", "Clean Room Solid Area", 96)
            sd.write_html('Device- 84.html', auto_open=True)
        elif self.n == 85 and self.z == 1:
            sd = no.read("C:/Users/noha.omar/Desktop/Govee1/yarb85_temp.csv",
                         "C:/Users/noha.omar/Desktop/Govee1/yarb85_hum.csv", "R&D Freezer", 96)
            sd.write_html('Device- 85.html', auto_open=True)
        elif self.n == 86 and self.z == 1:
            sd = no.read("C:/Users/noha.omar/Desktop/Govee1/yarb86_temp.csv",
                         "C:/Users/noha.omar/Desktop/Govee1/yarb86_hum.csv", "R&D Lab2", 96)
            sd.write_html('Device- 86.html', auto_open=True)
        elif self.n == 87 and self.z == 1:
            sd = no.read("C:/Users/noha.omar/Desktop/Govee1/yarb87_temp.csv",
                         "C:/Users/noha.omar/Desktop/Govee1/yarb87_hum.csv", "Incubator2", 96)
            sd.write_html('Device- 87.html', auto_open=True)
        elif self.n == 88 and self.z == 1:
            sd = no.read("C:/Users/noha.omar/Desktop/Govee1/yarb88_temp.csv",
                         "C:/Users/noha.omar/Desktop/Govee1/yarb88_hum.csv", "Incubator1", 96)
            sd.write_html('Device- 88.html', auto_open=True)
        elif self.n == 89 and self.z == 1:
            sd = no.read("C:/Users/noha.omar/Desktop/Govee1/yarb89_temp.csv",
                         "C:/Users/noha.omar/Desktop/Govee1/yarb89_hum.csv", "Incubator3", 96)
            sd.write_html('Device- 89.html', auto_open=True)
        elif self.n == 90 and self.z == 1:
            sd = no.read("C:/Users/noha.omar/Desktop/Govee1/yarb90_temp.csv",
                         "C:/Users/noha.omar/Desktop/Govee1/yarb90_hum.csv", "Incubator4", 96)
            sd.write_html('Device- 90.html', auto_open=True)
        elif self.n == 91 and self.z == 1:
            sd = no.read("C:/Users/noha.omar/Desktop/Govee1/yarb91_temp.csv",
                         "C:/Users/noha.omar/Desktop/Govee1/yarb91_hum.csv", "Micro fridge", 96)
            sd.write_html('Device- 91.html', auto_open=True)
        elif self.n == 93 and self.z == 1:
            sd = no.read("C:/Users/noha.omar/Desktop/Govee1/yarb93_temp.csv",
                         "C:/Users/noha.omar/Desktop/Govee1/yarb93_hum.csv", "Weighting Room 2", 96)
            sd.write_html('Device- 93.html', auto_open=True)
        elif self.n == 94 and self.z == 1:
            sd = no.read("C:/Users/noha.omar/Desktop/Govee1/yarb94_temp.csv",
                         "C:/Users/noha.omar/Desktop/Govee1/yarb94_hum.csv", "Retained Room 2", 96)
            sd.write_html('Device- 94.html', auto_open=True)
        elif self.n == 95 and self.z == 1:
            sd = no.read("C:/Users/noha.omar/Desktop/Govee1/yarb95_temp.csv",
                         "C:/Users/noha.omar/Desktop/Govee1/yarb95_hum.csv", "Clean Liquid Level2", 96)
            sd.write_html('Device- 95.html', auto_open=True)
        elif self.n == 96 and self.z == 1:
            sd = no.read("C:/Users/noha.omar/Desktop/Govee1/yarb96_temp.csv",
                         "C:/Users/noha.omar/Desktop/Govee1/yarb96_hum.csv", "Retained Room 1", 96)
            sd.write_html('Device- 95.html', auto_open=True)
        elif self.n == 97 and self.z == 1:
            sd = no.read("C:/Users/noha.omar/Desktop/Govee1/yarb97_temp.csv",
                         "C:/Users/noha.omar/Desktop/Govee1/yarb97_hum.csv", "Store Cold spot", 96)
            sd.write_html('Device- 95.html', auto_open=True)
        elif self.n == 98 and self.z == 1:
            sd = no.read("C:/Users/noha.omar/Desktop/Govee1/yarb98_temp.csv",
                         "C:/Users/noha.omar/Desktop/Govee1/yarb98_hum.csv", "Store hot spot", 96)
            sd.write_html('Device- 95.html', auto_open=True)

            # weeks

        elif self.n == 1 and self.z == 2:
            sd = no.read("C:/Users/noha.omar/Desktop/Govee1/yarb1_temp.csv",
                         "C:/Users/noha.omar/Desktop/Govee1/yarb1_hum.csv", "Seive", 672)
            sd.write_html('Device- 1.html', auto_open=True)
        elif self.n == 2 and self.z == 2:
            sd = no.read("C:/Users/noha.omar/Desktop/Govee1/yarb2_temp.csv",
                         "C:/Users/noha.omar/Desktop/Govee1/yarb2_hum.csv", "V Shape", 672)
            sd.write_html('Device- 2.html', auto_open=True)
        elif self.n == 3 and self.z == 2:
            sd = no.read("C:/Users/noha.omar/Desktop/Govee1/yarb3_temp.csv",
                         "C:/Users/noha.omar/Desktop/Govee1/yarb3_hum.csv", "Small Coating", 672)
            sd.write_html('Device- 3.html', auto_open=True)
        elif self.n == 4 and self.z == 2:
            sd = no.read("C:/Users/noha.omar/Desktop/Govee1/yarb4_temp.csv",
                         "C:/Users/noha.omar/Desktop/Govee1/yarb4_hum.csv", "Holding Room", 672)
            sd.write_html('Device- 4.html', auto_open=True)

        elif self.n == 5 and self.z == 2:
            sd = no.read("C:/Users/noha.omar/Desktop/Govee1/yarb5_temp.csv",
                         "C:/Users/noha.omar/Desktop/Govee1/yarb5_hum.csv", "Coating Gansons(Room2)", 672)
            sd.write_html('Device- 5.html', auto_open=True)

        elif self.n == 6 and self.z == 2:
            sd = no.read("C:/Users/noha.omar/Desktop/Govee1/yarb6_temp.csv",
                         "C:/Users/noha.omar/Desktop/Govee1/yarb6_hum.csv", "Sachet Filling2", 672)
            sd.write_html('Device- 6.html', auto_open=True)
        elif self.n == 7 and self.z == 2:
            sd = no.read("C:/Users/noha.omar/Desktop/Govee1/yarb7_temp.csv",
                         "C:/Users/noha.omar/Desktop/Govee1/yarb7_hum.csv", "Pilot(R&D Granulation)", 672)
            sd.write_html('Device- 7.html', auto_open=True)
        elif self.n == 8 and self.z == 2:
            sd = no.read("C:/Users/noha.omar/Desktop/Govee1/yarb8_temp.csv",
                         "C:/Users/noha.omar/Desktop/Govee1/yarb8_hum.csv", "R&D Blinding", 672)
            sd.write_html('Device- 8.html', auto_open=True)
        elif self.n == 9 and self.z == 2:
            sd = no.read("C:/Users/noha.omar/Desktop/Govee1/yarb9_temp.csv",
                         "C:/Users/noha.omar/Desktop/Govee1/yarb9_hum.csv", "R&D Compression", 672)
            sd.write_html('Device- 9.html', auto_open=True)
        elif self.n == 10 and self.z == 2:
            sd = no.read("C:/Users/noha.omar/Desktop/Govee1/yarb10_temp.csv",
                         "C:/Users/noha.omar/Desktop/Govee1/yarb10_hum.csv", "Holding Room (028P1)(Middle)", 672)
            sd.write_html('Device- 10.html', auto_open=True)

        elif self.n == 11 and self.z == 2:
            sd = no.read("C:/Users/noha.omar/Desktop/Govee1/yarb11_temp.csv",
                         "C:/Users/noha.omar/Desktop/Govee1/yarb11_hum.csv", "Capsule FillinG(Old)", 672)
            sd.write_html('Device- 11.html', auto_open=True)
        elif self.n == 12 and self.z == 2:
            sd = no.read("C:/Users/noha.omar/Desktop/Govee1/yarb12_temp.csv",
                         "C:/Users/noha.omar/Desktop/Govee1/yarb12_hum.csv", "Compresstion Room1", 672)
            sd.write_html('Device- 12.html', auto_open=True)
        elif self.n == 13 and self.z == 2:
            sd = no.read("C:/Users/noha.omar/Desktop/Govee1/yarb13_temp.csv",
                         "C:/Users/noha.omar/Desktop/Govee1/yarb13_hum.csv", "Granulation", 672)
            sd.write_html('Device- 13.html', auto_open=True)

        elif self.n == 14 and self.z == 2:
            sd = no.read("C:/Users/noha.omar/Desktop/Govee1/yarb14_temp.csv",
                         "C:/Users/noha.omar/Desktop/Govee1/yarb14_hum.csv", "Bin Blender", 672)
            sd.write_html('Device- 14.html', auto_open=True)

        elif self.n == 15 and self.z == 2:
            sd = no.read("C:/Users/noha.omar/Desktop/Govee1/yarb15_temp.csv",
                         "C:/Users/noha.omar/Desktop/Govee1/yarb15_hum.csv", "Compresstion Room2", 672)
            sd.write_html('Device- 15.html', auto_open=True)
        elif self.n == 16 and self.z == 2:
            sd = no.read("C:/Users/noha.omar/Desktop/Govee1/yarb16_temp.csv",
                         "C:/Users/noha.omar/Desktop/Govee1/yarb16_hum.csv", "Granulation", 672)
            sd.write_html('Device- 16.html', auto_open=True)
        elif self.n == 20 and self.z == 2:
            sd = no.read("C:/Users/noha.omar/Desktop/Govee1/yarb20_temp.csv",
                         "C:/Users/noha.omar/Desktop/Govee1/yarb20_hum.csv", "Depaking Room For Solid", 672)
            sd.write_html('Device- 20.html', auto_open=True)
        elif self.n == 21 and self.z == 2:
            sd = no.read("C:/Users/noha.omar/Desktop/Govee1/yarb21_temp.csv",
                         "C:/Users/noha.omar/Desktop/Govee1/yarb21_hum.csv", "Bottle Clean For Dry Syrup", 672)
            sd.write_html('Device- 21.html', auto_open=True)
        elif self.n == 22 and self.z == 2:
            sd = no.read("C:/Users/noha.omar/Desktop/Govee1/yarb22_temp.csv",
                         "C:/Users/noha.omar/Desktop/Govee1/yarb22_hum.csv", " Dry Syrup Filling", 672)
            sd.write_html('Device- 22.html', auto_open=True)
        elif self.n == 23 and self.z == 2:
            sd = no.read("C:/Users/noha.omar/Desktop/Govee1/yarb23_temp.csv",
                         "C:/Users/noha.omar/Desktop/Govee1/yarb23_hum.csv", "Sachet FillinG(Old)", 672)
            sd.write_html('Device- 23.html', auto_open=True)

        elif self.n == 24 and self.z == 2:
            sd = no.read("C:/Users/noha.omar/Desktop/Govee1/yarb24_temp.csv",
                         "C:/Users/noha.omar/Desktop/Govee1/yarb24_hum.csv", "Coating Solution Prep ", 672)
            sd.write_html('Device- 24.html', auto_open=True)
        elif self.n == 25 and self.z == 2:
            sd = no.read("C:/Users/noha.omar/Desktop/Govee1/yarb25_temp.csv",
                         "C:/Users/noha.omar/Desktop/Govee1/yarb25_hum.csv", "Capsule Filling 2 ", 672)
            sd.write_html('Device- 25.html', auto_open=True)
        elif self.n == 26 and self.z == 2:
            sd = no.read("C:/Users/noha.omar/Desktop/Govee1/yarb26_temp.csv",
                         "C:/Users/noha.omar/Desktop/Govee1/yarb26_hum.csv", "Coating Room 1(Old) ", 672)
            sd.write_html('Device- 26.html', auto_open=True)
        elif self.n == 27 and self.z == 2:
            sd = no.read("C:/Users/noha.omar/Desktop/Govee1/yarb27_temp.csv",
                         "C:/Users/noha.omar/Desktop/Govee1/yarb27_hum.csv", "Corridor Against  sacchet Filling ", 672)
            sd.write_html('Device- 27.html', auto_open=True)

        elif self.n == 28 and self.z == 2:
            sd = no.read("C:/Users/noha.omar/Desktop/Govee1/yarb28_temp.csv",
                         "C:/Users/noha.omar/Desktop/Govee1/yarb28_hum.csv", "Corridor Against V Shape ", 672)
            sd.write_html('Device- 28.html', auto_open=True)

        elif self.n == 29 and self.z == 2:
            sd = no.read("C:/Users/noha.omar/Desktop/Govee1/yarb29_temp.csv",
                         "C:/Users/noha.omar/Desktop/Govee1/yarb29_hum.csv", "Stage Out (Solid area)", 672)
            sd.write_html('Device- 29.html', auto_open=True)
        elif self.n == 30 and self.z == 2:
            sd = no.read("C:/Users/noha.omar/Desktop/Govee1/yarb30_temp.csv",
                         "C:/Users/noha.omar/Desktop/Govee1/yarb30_hum.csv", "Corridor Against IPC ", 672)
            sd.write_html('Device- 30.html', auto_open=True)
        elif self.n == 31 and self.z == 2:
            sd = no.read("C:/Users/noha.omar/Desktop/Govee1/yarb31_temp.csv",
                         "C:/Users/noha.omar/Desktop/Govee1/yarb31_hum.csv", "MAl (Solid area)", 672)
            sd.write_html('Device- 31.html', auto_open=True)
        elif self.n == 32 and self.z == 2:
            sd = no.read("C:/Users/noha.omar/Desktop/Govee1/yarb32_temp.csv",
                         "C:/Users/noha.omar/Desktop/Govee1/yarb32_hum.csv", "Cleaning Room for Liquid bottle1(Old)",
                         672)
            sd.write_html('Device- 32.html', auto_open=True)
        elif self.n == 33 and self.z == 2:
            sd = no.read("C:/Users/noha.omar/Desktop/Govee1/yarb33_temp.csv",
                         "C:/Users/noha.omar/Desktop/Govee1/yarb33_hum.csv", "Filling Room for Liquid 1(Old)", 672)
            sd.write_html('Device- 33.html', auto_open=True)
        elif self.n == 34 and self.z == 2:
            sd = no.read("C:/Users/noha.omar/Desktop/Govee1/yarb34_temp.csv",
                         "C:/Users/noha.omar/Desktop/Govee1/yarb34_hum.csv", "Cleaning Room for Liquid bottle2(new)",
                         672)
            sd.write_html('Device- 34.html', auto_open=True)

        elif self.n == 35 and self.z == 2:
            sd = no.read("C:/Users/noha.omar/Desktop/Govee1/yarb35_temp.csv",
                         "C:/Users/noha.omar/Desktop/Govee1/yarb35_hum.csv", "Filling Room for Liquid 2(new)", 672)
            sd.write_html('Device- 35.html', auto_open=True)

        elif self.n == 36 and self.z == 2:
            sd = no.read("C:/Users/noha.omar/Desktop/Govee1/yarb36_temp.csv",
                         "C:/Users/noha.omar/Desktop/Govee1/yarb36_hum.csv", "MAL 1 Inner Part", 672)
            sd.write_html('Device- 36.html', auto_open=True)
        elif self.n == 37 and self.z == 2:
            sd = no.read("C:/Users/noha.omar/Desktop/Govee1/yarb37_temp.csv",
                         "C:/Users/noha.omar/Desktop/Govee1/yarb37_hum.csv", "MAL 1 Outer Part", 672)
            sd.write_html('Device- 37.html', auto_open=True)
        elif self.n == 38 and self.z == 2:
            sd = no.read("C:/Users/noha.omar/Desktop/Govee1/yarb38_temp.csv",
                         "C:/Users/noha.omar/Desktop/Govee1/yarb38_hum.csv", "MAL 2 Inner Part", 672)
            sd.write_html('Device- 38.html', auto_open=True)

        elif self.n == 39 and self.z == 2:
            sd = no.read("C:/Users/noha.omar/Desktop/Govee1/yarb39_temp.csv",
                         "C:/Users/noha.omar/Desktop/Govee1/yarb39_hum.csv", "MAL 2 Outer Part", 672)
            sd.write_html('Device- 39.html', auto_open=True)

        elif self.n == 40 and self.z == 2:
            sd = no.read("C:/Users/noha.omar/Desktop/Govee1/yarb40_temp.csv",
                         "C:/Users/noha.omar/Desktop/Govee1/yarb40_hum.csv", "Corridor Liquid First Floor", 672)
            sd.write_html('Device- 40.html', auto_open=True)

        elif self.n == 41 and self.z == 2:
            sd = no.read("C:/Users/noha.omar/Desktop/Govee1/yarb41_temp.csv",
                         "C:/Users/noha.omar/Desktop/Govee1/yarb41_hum.csv", "SS2 Packaging Syrup", 672)
            sd.write_html('Device- 41.html', auto_open=True)

        elif self.n == 42 and self.z == 2:
            sd = no.read("C:/Users/noha.omar/Desktop/Govee1/yarb42_temp.csv",
                         "C:/Users/noha.omar/Desktop/Govee1/yarb42_hum.csv", "Syrup Packaging EMA Safe", 672)
            sd.write_html('Device- 42.html', auto_open=True)
        elif self.n == 43 and self.z == 2:
            sd = no.read("C:/Users/noha.omar/Desktop/Govee1/yarb43_temp.csv",
                         "C:/Users/noha.omar/Desktop/Govee1/yarb43_hum.csv", "Semisolid Filling 3", 672)
            sd.write_html('Device- 43.html', auto_open=True)
        elif self.n == 44 and self.z == 2:
            sd = no.read("C:/Users/noha.omar/Desktop/Govee1/yarb44_temp.csv",
                         "C:/Users/noha.omar/Desktop/Govee1/yarb44_hum.csv", "Sk (Liq.Prep 2)", 672)
            sd.write_html('Device- 44.html', auto_open=True)
        elif self.n == 45 and self.z == 2:
            sd = no.read("C:/Users/noha.omar/Desktop/Govee1/yarb45_temp.csv",
                         "C:/Users/noha.omar/Desktop/Govee1/yarb45_hum.csv", "Fryma Old (Cream Prep)", 672)
            sd.write_html('Device- 45.html', auto_open=True)
        elif self.n == 46 and self.z == 2:
            sd = no.read("C:/Users/noha.omar/Desktop/Govee1/yarb46_temp.csv",
                         "C:/Users/noha.omar/Desktop/Govee1/yarb46_hum.csv", "Fryma New (Semisolid Prep)", 672)
            sd.write_html('Device- 46.html', auto_open=True)

        elif self.n == 47 and self.z == 2:
            sd = no.read("C:/Users/noha.omar/Desktop/Govee1/yarb47_temp.csv",
                         "C:/Users/noha.omar/Desktop/Govee1/yarb47_hum.csv", "Liq . Prep 1(Old)", 672)
            sd.write_html('Device- 47.html', auto_open=True)

        elif self.n == 48 and self.z == 2:
            sd = no.read("C:/Users/noha.omar/Desktop/Govee1/yarb48_temp.csv",
                         "C:/Users/noha.omar/Desktop/Govee1/yarb48_hum.csv", "Axomatic New (Semisolid Filling 2)", 672)
            sd.write_html('Device- 48.html', auto_open=True)
        elif self.n == 49 and self.z == 2:
            sd = no.read("C:/Users/noha.omar/Desktop/Govee1/yarb49_temp.csv",
                         "C:/Users/noha.omar/Desktop/Govee1/yarb49_hum.csv", "Axomatic Old (Semisolid Filling 1)", 672)
            sd.write_html('Device- 49.html', auto_open=True)
        elif self.n == 50 and self.z == 2:
            sd = no.read("C:/Users/noha.omar/Desktop/Govee1/yarb50_temp.csv",
                         "C:/Users/noha.omar/Desktop/Govee1/yarb50_hum.csv", "Ext. Prep Room", 672)
            sd.write_html('Device- 50.html', auto_open=True)

        elif self.n == 51 and self.z == 2:
            sd = no.read("C:/Users/noha.omar/Desktop/Govee1/yarb51_temp.csv",
                         "C:/Users/noha.omar/Desktop/Govee1/yarb51_hum.csv", "Ext. Cleaning Line", 672)
            sd.write_html('Device- 51.html', auto_open=True)

        elif self.n == 52 and self.z == 2:
            sd = no.read("C:/Users/noha.omar/Desktop/Govee1/yarb52_temp.csv",
                         "C:/Users/noha.omar/Desktop/Govee1/yarb52_hum.csv", "Ext. Filling Line", 672)
            sd.write_html('Device- 52.html', auto_open=True)
        elif self.n == 53 and self.z == 2:
            sd = no.read("C:/Users/noha.omar/Desktop/Govee1/yarb53_temp.csv",
                         "C:/Users/noha.omar/Desktop/Govee1/yarb53_hum.csv", "Depaking Room for Liquid", 672)
            sd.write_html('Device- 53.html', auto_open=True)
        elif self.n == 54 and self.z == 2:
            sd = no.read("C:/Users/noha.omar/Desktop/Govee1/yarb54_temp.csv",
                         "C:/Users/noha.omar/Desktop/Govee1/yarb54_hum.csv", "Corridor in Liquid area(2nd Floor)", 672)
            sd.write_html('Device- 54.html', auto_open=True)

        elif self.n == 55 and self.z == 2:
            sd = no.read("C:/Users/noha.omar/Desktop/Govee1/yarb55_temp.csv",
                         "C:/Users/noha.omar/Desktop/Govee1/yarb55_hum.csv", "MAl Semisolid Inner Part", 672)
            sd.write_html('Device- 55.html', auto_open=True)

        elif self.n == 56 and self.z == 2:
            sd = no.read("C:/Users/noha.omar/Desktop/Govee1/yarb56_temp.csv",
                         "C:/Users/noha.omar/Desktop/Govee1/yarb56_hum.csv", "MAl Semisolid Outer Part", 672)
            sd.write_html('Device- 56.html', auto_open=True)
        elif self.n == 57 and self.z == 2:
            sd = no.read("C:/Users/noha.omar/Desktop/Govee1/yarb57_temp.csv",
                         "C:/Users/noha.omar/Desktop/Govee1/yarb57_hum.csv", "Partina (Blistering Room 1)", 672)
            sd.write_html('Device- 57.html', auto_open=True)
        elif self.n == 58 and self.z == 2:
            sd = no.read("C:/Users/noha.omar/Desktop/Govee1/yarb58_temp.csv",
                         "C:/Users/noha.omar/Desktop/Govee1/yarb58_hum.csv", "Tablet Counter Room", 672)
            sd.write_html('Device- 58.html', auto_open=True)

        elif self.n == 59 and self.z == 2:
            sd = no.read("C:/Users/noha.omar/Desktop/Govee1/yarb59_temp.csv",
                         "C:/Users/noha.omar/Desktop/Govee1/yarb59_hum.csv", "Pam New (Bilistering 3)", 672)
            sd.write_html('Device- 59.html', auto_open=True)

        elif self.n == 60 and self.z == 2:
            sd = no.read("C:/Users/noha.omar/Desktop/Govee1/yarb60_temp.csv",
                         "C:/Users/noha.omar/Desktop/Govee1/yarb60_hum.csv", "Pam Old (Bilistering 2)", 672)
            sd.write_html('Device- 60.html', auto_open=True)
        elif self.n == 61 and self.z == 2:
            sd = no.read("C:/Users/noha.omar/Desktop/Govee1/yarb61_temp.csv",
                         "C:/Users/noha.omar/Desktop/Govee1/yarb61_hum.csv", "MAL Bilistering ", 672)
            sd.write_html('Device- 61.html', auto_open=True)
        elif self.n == 62 and self.z == 2:
            sd = no.read("C:/Users/noha.omar/Desktop/Govee1/yarb62_temp.csv",
                         "C:/Users/noha.omar/Desktop/Govee1/yarb62_hum.csv", " Bilistering  Corridor", 672)
            sd.write_html('Device- 62.html', auto_open=True)

        elif self.n == 63 and self.z == 2:
            sd = no.read("C:/Users/noha.omar/Desktop/Govee1/yarb63_temp.csv",
                         "C:/Users/noha.omar/Desktop/Govee1/yarb63_hum.csv", " SS (Packaging Machine)", 672)
            sd.write_html('Device- 63.html', auto_open=True)

        elif self.n == 64 and self.z == 2:
            sd = no.read("C:/Users/noha.omar/Desktop/Govee1/yarb64_temp.csv",
                         "C:/Users/noha.omar/Desktop/Govee1/yarb64_hum.csv", " Packaging Blister", 672)
            sd.write_html('Device- 64.html', auto_open=True)
        elif self.n == 65 and self.z == 2:
            sd = no.read("C:/Users/noha.omar/Desktop/Govee1/yarb65_temp.csv",
                         "C:/Users/noha.omar/Desktop/Govee1/yarb65_hum.csv", " Pamphlet Area (Metronic Machine)", 672)
            sd.write_html('Device- 65.html', auto_open=True)
        elif self.n == 66 and self.z == 2:
            sd = no.read("C:/Users/noha.omar/Desktop/Govee1/yarb66_temp.csv",
                         "C:/Users/noha.omar/Desktop/Govee1/yarb66_hum.csv", " Holding Room Packaging Area", 672)
            sd.write_html('Device- 66.html', auto_open=True)

        elif self.n == 67 and self.z == 2:
            sd = no.read("C:/Users/noha.omar/Desktop/Govee1/yarb67_temp.csv",
                         "C:/Users/noha.omar/Desktop/Govee1/yarb67_hum.csv", " Weight Room 1", 672)
            sd.write_html('Device- 67.html', auto_open=True)

        elif self.n == 68 and self.z == 2:
            sd = no.read("C:/Users/noha.omar/Desktop/Govee1/yarb68_temp.csv",
                         "C:/Users/noha.omar/Desktop/Govee1/yarb68_hum.csv", " Weight Room 2", 672)
            sd.write_html('Device- 68.html', auto_open=True)

        elif self.n == 69 and self.z == 2:
            sd = no.read("C:/Users/noha.omar/Desktop/Govee1/yarb69_temp.csv",
                         "C:/Users/noha.omar/Desktop/Govee1/yarb69_hum.csv", " Weight Corridor", 672)
            sd.write_html('Device- 69.html', auto_open=True)
        elif self.n == 70 and self.z == 2:
            sd = no.read("C:/Users/noha.omar/Desktop/Govee1/yarb70_temp.csv",
                         "C:/Users/noha.omar/Desktop/Govee1/yarb70_hum.csv", "Sampling", 672)
            sd.write_html('Device- 70.html', auto_open=True)
        elif self.n == 71 and self.z == 2:
            sd = no.read("C:/Users/noha.omar/Desktop/Govee1/yarb71_temp.csv",
                         "C:/Users/noha.omar/Desktop/Govee1/yarb71_hum.csv", "QC Fridge", 672)
            sd.write_html('Device- 71.html', auto_open=True)
        elif self.n == 72 and self.z == 2:
            sd = no.read("C:/Users/noha.omar/Desktop/Govee1/yarb72_temp.csv",
                         "C:/Users/noha.omar/Desktop/Govee1/yarb72_hum.csv", "QC Freezer", 672)
            sd.write_html('Device- 72.html', auto_open=True)
        elif self.n == 73 and self.z == 2:
            sd = no.read("C:/Users/noha.omar/Desktop/Govee1/yarb73_temp.csv",
                         "C:/Users/noha.omar/Desktop/Govee1/yarb73_hum.csv", "Packaging (Pd Sticking Machine)", 672)
            sd.write_html('Device- 73.html', auto_open=True)
        elif self.n == 74 and self.z == 2:
            sd = no.read("C:/Users/noha.omar/Desktop/Govee1/yarb74_temp.csv",
                         "C:/Users/noha.omar/Desktop/Govee1/yarb74_hum.csv", "CIP (2nd Floor)", 672)
            sd.write_html('Device- 74.html', auto_open=True)
        elif self.n == 75 and self.z == 2:
            sd = no.read("C:/Users/noha.omar/Desktop/Govee1/yarb75_temp.csv",
                         "C:/Users/noha.omar/Desktop/Govee1/yarb75_hum.csv", "Cold Store", 672)
            sd.write_html('Device- 75.html', auto_open=True)
        elif self.n == 76 and self.z == 2:
            sd = no.read("C:/Users/noha.omar/Desktop/Govee1/yarb76_temp.csv",
                         "C:/Users/noha.omar/Desktop/Govee1/yarb76_hum.csv", "Small Stability", 672)
            sd.write_html('Device- 76.html', auto_open=True)
        elif self.n == 77 and self.z == 2:
            sd = no.read("C:/Users/noha.omar/Desktop/Govee1/yarb77_temp.csv",
                         "C:/Users/noha.omar/Desktop/Govee1/yarb77_hum.csv", "Large Stability", 672)
            sd.write_html('Device- 77.html', auto_open=True)
        elif self.n == 78 and self.z == 2:
            sd = no.read("C:/Users/noha.omar/Desktop/Govee1/yarb78_temp.csv",
                         "C:/Users/noha.omar/Desktop/Govee1/yarb78_hum.csv", "R&D LAB", 672)
            sd.write_html('Device- 78.html', auto_open=True)
        elif self.n == 79 and self.z == 2:
            sd = no.read("C:/Users/noha.omar/Desktop/Govee1/yarb79_temp.csv",
                         "C:/Users/noha.omar/Desktop/Govee1/yarb79_hum.csv", "R&D Fridge", 672)
            sd.write_html('Device- 79.html', auto_open=True)
        elif self.n == 80 and self.z == 1:
            sd = no.read("C:/Users/noha.omar/Desktop/Govee1/yarb80_temp.csv",
                         "C:/Users/noha.omar/Desktop/Govee1/yarb80_hum.csv", "QC", 672)
            sd.write_html('Device- 80.html', auto_open=True)

        elif self.n == 81 and self.z == 2:
            sd = no.read("C:/Users/noha.omar/Desktop/Govee1/yarb81_temp.csv",
                         "C:/Users/noha.omar/Desktop/Govee1/yarb81_hum.csv", "Cleaning room for liquid bottle 1(old)",
                         672)
            sd.write_html('Device- 81.html', auto_open=True)
        elif self.n == 82 and self.z == 2:
            sd = no.read("C:/Users/noha.omar/Desktop/Govee1/yarb82_temp.csv",
                         "C:/Users/noha.omar/Desktop/Govee1/yarb82_hum.csv", "MAL 1 OUTER PART", 672)
            sd.write_html('Device- 82.html', auto_open=True)
        elif self.n == 83 and self.z == 2:
            sd = no.read("C:/Users/noha.omar/Desktop/Govee1/yarb83_temp.csv",
                         "C:/Users/noha.omar/Desktop/Govee1/yarb83_hum.csv", "MAL 2 OUTER PART", 672)
            sd.write_html('Device- 83.html', auto_open=True)
        elif self.n == 84 and self.z == 2:
            sd = no.read("C:/Users/noha.omar/Desktop/Govee1/yarb84_temp.csv",
                         "C:/Users/noha.omar/Desktop/Govee1/yarb84_hum.csv", "Clean Room Solid Area", 672)
            sd.write_html('Device- 84.html', auto_open=True)
        elif self.n == 85 and self.z == 2:
            sd = no.read("C:/Users/noha.omar/Desktop/Govee1/yarb85_temp.csv",
                         "C:/Users/noha.omar/Desktop/Govee1/yarb85_hum.csv", "R&D Freezer", 672)
            sd.write_html('Device- 85.html', auto_open=True)
        elif self.n == 86 and self.z == 2:
            sd = no.read("C:/Users/noha.omar/Desktop/Govee1/yarb86_temp.csv",
                         "C:/Users/noha.omar/Desktop/Govee1/yarb86_hum.csv", "R&D Lab2", 672)
            sd.write_html('Device- 79.html', auto_open=True)
        elif self.n == 87 and self.z == 2:
            sd = no.read("C:/Users/noha.omar/Desktop/Govee1/yarb87_temp.csv",
                         "C:/Users/noha.omar/Desktop/Govee1/yarb87_hum.csv", "Incubator2", 672)
            sd.write_html('Device- 87.html', auto_open=True)
        elif self.n == 88 and self.z == 2:
            sd = no.read("C:/Users/noha.omar/Desktop/Govee1/yarb88_temp.csv",
                         "C:/Users/noha.omar/Desktop/Govee1/yarb88_hum.csv", "Incubator1", 672)
            sd.write_html('Device- 88.html', auto_open=True)
        elif self.n == 89 and self.z == 2:
            sd = no.read("C:/Users/noha.omar/Desktop/Govee1/yarb89_temp.csv",
                         "C:/Users/noha.omar/Desktop/Govee1/yarb89_hum.csv", "Incubator3", 672)
            sd.write_html('Device- 89.html', auto_open=True)
        elif self.n == 90 and self.z == 2:
            sd = no.read("C:/Users/noha.omar/Desktop/Govee1/yarb90_temp.csv",
                         "C:/Users/noha.omar/Desktop/Govee1/yarb90_hum.csv", "Incubator4", 672)
            sd.write_html('Device- 90.html', auto_open=True)
        elif self.n == 91 and self.z == 2:
            sd = no.read("C:/Users/noha.omar/Desktop/Govee1/yarb91_temp.csv",
                         "C:/Users/noha.omar/Desktop/Govee1/yarb91_hum.csv", "Micro fridge", 672)
            sd.write_html('Device- 91.html', auto_open=True)
        elif self.n == 93 and self.z == 2:
            sd = no.read("C:/Users/noha.omar/Desktop/Govee1/yarb93_temp.csv",
                         "C:/Users/noha.omar/Desktop/Govee1/yarb93_hum.csv", "Weighting Room 2", 672)
            sd.write_html('Device- 93.html', auto_open=True)
        elif self.n == 94 and self.z == 2:
            sd = no.read("C:/Users/noha.omar/Desktop/Govee1/yarb94_temp.csv",
                         "C:/Users/noha.omar/Desktop/Govee1/yarb94_hum.csv", "Retained Room 2", 672)
            sd.write_html('Device- 94.html', auto_open=True)
        elif self.n == 95 and self.z == 2:
            sd = no.read("C:/Users/noha.omar/Desktop/Govee1/yarb95_temp.csv",
                         "C:/Users/noha.omar/Desktop/Govee1/yarb95_hum.csv", "Clean Liquid Level2", 672)
            sd.write_html('Device- 95.html', auto_open=True)
        elif self.n == 96 and self.z == 2:
            sd = no.read("C:/Users/noha.omar/Desktop/Govee1/yarb96_temp.csv",
                         "C:/Users/noha.omar/Desktop/Govee1/yarb96_hum.csv", "Retained Room 1", 672)
            sd.write_html('Device- 95.html', auto_open=True)
        elif self.n == 97 and self.z == 2:
            sd = no.read("C:/Users/noha.omar/Desktop/Govee1/yarb97_temp.csv",
                         "C:/Users/noha.omar/Desktop/Govee1/yarb97_hum.csv", "Store Cold spot", 672)
            sd.write_html('Device- 95.html', auto_open=True)
        elif self.n == 98 and self.z == 2:
            sd = no.read("C:/Users/noha.omar/Desktop/Govee1/yarb98_temp.csv",
                         "C:/Users/noha.omar/Desktop/Govee1/yarb98_hum.csv", "Store hot spot", 672)
            sd.write_html('Device- 95.html', auto_open=True)

            # months

        elif self.n == 1 and self.z == 3:
            sd = no.read("C:/Users/noha.omar/Desktop/Govee1/yarb1_temp.csv",
                         "C:/Users/noha.omar/Desktop/Govee1/yarb1_hum.csv", "Seive", 2976)
            sd.write_html('Device- 1.html', auto_open=True)
        elif self.n == 2 and self.z == 3:
            sd = no.read("C:/Users/noha.omar/Desktop/Govee1/yarb2_temp.csv",
                         "C:/Users/noha.omar/Desktop/Govee1/yarb2_hum.csv", "V Shape", 2976)
            sd.write_html('Device- 2.html', auto_open=True)
        elif self.n == 3 and self.z == 3:
            sd = no.read("C:/Users/noha.omar/Desktop/Govee1/yarb3_temp.csv",
                         "C:/Users/noha.omar/Desktop/Govee1/yarb3_hum.csv", "Small Coating", 2976)
            sd.write_html('Device- 3.html', auto_open=True)

        elif self.n == 4 and self.z == 3:
            sd = no.read("C:/Users/noha.omar/Desktop/Govee1/yarb4_temp.csv",
                         "C:/Users/noha.omar/Desktop/Govee1/yarb4_hum.csv", "Holding Room", 2976)
            sd.write_html('Device- 4.html', auto_open=True)
        elif self.n == 5 and self.z == 3:
            sd = no.read("C:/Users/noha.omar/Desktop/Govee1/yarb5_temp.csv",
                         "C:/Users/noha.omar/Desktop/Govee1/yarb5_hum.csv", "Coating Gansons(Room2)", 2976)
            sd.write_html('Device- 5.html', auto_open=True)

        elif self.n == 6 and self.z == 3:
            sd = no.read("C:/Users/noha.omar/Desktop/Govee1/yarb6_temp.csv",
                         "C:/Users/noha.omar/Desktop/Govee1/yarb6_hum.csv", "Sachet Filling2", 2976)
            sd.write_html('Device- 6.html', auto_open=True)
        elif self.n == 7 and self.z == 3:
            sd = no.read("C:/Users/noha.omar/Desktop/Govee1/yarb7_temp.csv",
                         "C:/Users/noha.omar/Desktop/Govee1/yarb7_hum.csv", "Pilot(R&D Granulation)", 2976)
            sd.write_html('Device- 7.html', auto_open=True)
        elif self.n == 8 and self.z == 3:
            sd = no.read("C:/Users/noha.omar/Desktop/Govee1/yarb8_temp.csv",
                         "C:/Users/noha.omar/Desktop/Govee1/yarb8_hum.csv", "R&D Blinding", 2976)
            sd.write_html('Device- 8.html', auto_open=True)
        elif self.n == 9 and self.z == 3:
            sd = no.read("C:/Users/noha.omar/Desktop/Govee1/yarb9_temp.csv",
                         "C:/Users/noha.omar/Desktop/Govee1/yarb9_hum.csv", "R&D Compression", 2976)
            sd.write_html('Device- 9.html', auto_open=True)
        elif self.n == 10 and self.z == 3:
            sd = no.read("C:/Users/noha.omar/Desktop/Govee1/yarb10_temp.csv",
                         "C:/Users/noha.omar/Desktop/Govee1/yarb10_hum.csv", "Holding Room (028P1)(Middle)", 2976)
            sd.write_html('Device- 10.html', auto_open=True)

        elif self.n == 11 and self.z == 3:
            sd = no.read("C:/Users/noha.omar/Desktop/Govee1/yarb11_temp.csv",
                         "C:/Users/noha.omar/Desktop/Govee1/yarb11_hum.csv", "Capsule FillinG(Old)", 2976)
            sd.write_html('Device- 11.html', auto_open=True)

        elif self.n == 12 and self.z == 3:
            sd = no.read("C:/Users/noha.omar/Desktop/Govee1/yarb12_temp.csv",
                         "C:/Users/noha.omar/Desktop/Govee1/yarb12_hum.csv", "Compresstion Room1", 2976)
            sd.write_html('Device- 12.html', auto_open=True)
        elif self.n == 13 and self.z == 3:
            sd = no.read("C:/Users/noha.omar/Desktop/Govee1/yarb13_temp.csv",
                         "C:/Users/noha.omar/Desktop/Govee1/yarb13_hum.csv", "Granulation", 2976)
            sd.write_html('Device- 13.html', auto_open=True)

        elif self.n == 14 and self.z == 3:
            sd = no.read("C:/Users/noha.omar/Desktop/Govee1/yarb14_temp.csv",
                         "C:/Users/noha.omar/Desktop/Govee1/yarb14_hum.csv", "Bin Blender", 2976)
            sd.write_html('Device- 14.html', auto_open=True)
        elif self.n == 15 and self.z == 3:
            sd = no.read("C:/Users/noha.omar/Desktop/Govee1/yarb15_temp.csv",
                         "C:/Users/noha.omar/Desktop/Govee1/yarb15_hum.csv", "Compresstion Room2", 2976)
            sd.write_html('Device- 15.html', auto_open=True)
        elif self.n == 16 and self.z == 3:
            sd = no.read("C:/Users/noha.omar/Desktop/Govee1/yarb16_temp.csv",
                         "C:/Users/noha.omar/Desktop/Govee1/yarb16_hum.csv", "Granulation", 2976)
            sd.write_html('Device- 16.html', auto_open=True)

        elif self.n == 20 and self.z == 3:
            sd = no.read("C:/Users/noha.omar/Desktop/Govee1/yarb20_temp.csv",
                         "C:/Users/noha.omar/Desktop/Govee1/yarb20_hum.csv", "Depaking Room For Solid", 2976)
            sd.write_html('Device- 20.html', auto_open=True)
        elif self.n == 21 and self.z == 3:
            sd = no.read("C:/Users/noha.omar/Desktop/Govee1/yarb21_temp.csv",
                         "C:/Users/noha.omar/Desktop/Govee1/yarb21_hum.csv", "Bottle Clean For Dry Syrup", 2976)
            sd.write_html('Device- 21.html', auto_open=True)
        elif self.n == 22 and self.z == 3:
            sd = no.read("C:/Users/noha.omar/Desktop/Govee1/yarb22_temp.csv",
                         "C:/Users/noha.omar/Desktop/Govee1/yarb22_hum.csv", " Dry Syrup Filling", 2976)
            sd.write_html('Device- 22.html', auto_open=True)
        elif self.n == 23 and self.z == 3:
            sd = no.read("C:/Users/noha.omar/Desktop/Govee1/yarb23_temp.csv",
                         "C:/Users/noha.omar/Desktop/Govee1/yarb23_hum.csv", "Sachet FillinG(Old)", 2976)
            sd.write_html('Device- 23.html', auto_open=True)
        elif self.n == 24 and self.z == 3:
            sd = no.read("C:/Users/noha.omar/Desktop/Govee1/yarb24_temp.csv",
                         "C:/Users/noha.omar/Desktop/Govee1/yarb24_hum.csv", "Coating Solution Prep ", 2976)
            sd.write_html('Device- 24.html', auto_open=True)

        elif self.n == 25 and self.z == 3:
            sd = no.read("C:/Users/noha.omar/Desktop/Govee1/yarb25_temp.csv",
                         "C:/Users/noha.omar/Desktop/Govee1/yarb25_hum.csv", "Capsule Filling 2 ", 2976)
            sd.write_html('Device- 25.html', auto_open=True)

        elif self.n == 26 and self.z == 3:
            sd = no.read("C:/Users/noha.omar/Desktop/Govee1/yarb26_temp.csv",
                         "C:/Users/noha.omar/Desktop/Govee1/yarb26_hum.csv", "Coating Room 1(Old) ", 2976)
            sd.write_html('Device- 26.html', auto_open=True)
        elif self.n == 27 and self.z == 3:
            sd = no.read("C:/Users/noha.omar/Desktop/Govee1/yarb27_temp.csv",
                         "C:/Users/noha.omar/Desktop/Govee1/yarb27_hum.csv", "Corridor Against  sacchet Filling ", 2976)
            sd.write_html('Device- 27.html', auto_open=True)

        elif self.n == 28 and self.z == 3:
            sd = no.read("C:/Users/noha.omar/Desktop/Govee1/yarb28_temp.csv",
                         "C:/Users/noha.omar/Desktop/Govee1/yarb28_hum.csv", "Corridor Against V Shape ", 2976)
            sd.write_html('Device- 28.html', auto_open=True)
        elif self.n == 29 and self.z == 3:
            sd = no.read("C:/Users/noha.omar/Desktop/Govee1/yarb29_temp.csv",
                         "C:/Users/noha.omar/Desktop/Govee1/yarb29_hum.csv", "Stage Out (Solid area)", 2976)
            sd.write_html('Device- 29.html', auto_open=True)

        elif self.n == 30 and self.z == 3:
            sd = no.read("C:/Users/noha.omar/Desktop/Govee1/yarb30_temp.csv",
                         "C:/Users/noha.omar/Desktop/Govee1/yarb30_hum.csv", "Corridor Against IPC ", 2976)
            sd.write_html('Device- 30.html', auto_open=True)
        elif self.n == 31 and self.z == 3:
            sd = no.read("C:/Users/noha.omar/Desktop/Govee1/yarb31_temp.csv",
                         "C:/Users/noha.omar/Desktop/Govee1/yarb31_hum.csv", "MAl (Solid area)", 2976)
            sd.write_html('Device- 31.html', auto_open=True)
        elif self.n == 32 and self.z == 3:
            sd = no.read("C:/Users/noha.omar/Desktop/Govee1/yarb32_temp.csv",
                         "C:/Users/noha.omar/Desktop/Govee1/yarb32_hum.csv", "Cleaning Room for Liquid bottle1(Old)",
                         2976)
            sd.write_html('Device- 32.html', auto_open=True)
        elif self.n == 33 and self.z == 3:
            sd = no.read("C:/Users/noha.omar/Desktop/Govee1/yarb33_temp.csv",
                         "C:/Users/noha.omar/Desktop/Govee1/yarb33_hum.csv", "Filling Room for Liquid 1(Old)", 2976)
            sd.write_html('Device- 33.html', auto_open=True)
        elif self.n == 34 and self.z == 3:
            sd = no.read("C:/Users/noha.omar/Desktop/Govee1/yarb34_temp.csv",
                         "C:/Users/noha.omar/Desktop/Govee1/yarb34_hum.csv", "Cleaning Room for Liquid bottle2(new)",
                         2976)
            sd.write_html('Device- 34.html', auto_open=True)
        elif self.n == 35 and self.z == 3:
            sd = no.read("C:/Users/noha.omar/Desktop/Govee1/yarb35_temp.csv",
                         "C:/Users/noha.omar/Desktop/Govee1/yarb35_hum.csv", "Filling Room for Liquid 2(new)", 2976)
            sd.write_html('Device- 35.html', auto_open=True)

        elif self.n == 36 and self.z == 3:
            sd = no.read("C:/Users/noha.omar/Desktop/Govee1/yarb36_temp.csv",
                         "C:/Users/noha.omar/Desktop/Govee1/yarb36_hum.csv", "MAL 1 Inner Part", 2976)
            sd.write_html('Device- 36.html', auto_open=True)

        elif self.n == 37 and self.z == 3:
            sd = no.read("C:/Users/noha.omar/Desktop/Govee1/yarb37_temp.csv",
                         "C:/Users/noha.omar/Desktop/Govee1/yarb37_hum.csv", "MAL 1 Outer Part", 2976)
            sd.write_html('Device- 37.html', auto_open=True)
        elif self.n == 38 and self.z == 3:
            sd = no.read("C:/Users/noha.omar/Desktop/Govee1/yarb38_temp.csv",
                         "C:/Users/noha.omar/Desktop/Govee1/yarb38_hum.csv", "MAL 2 Inner Part", 2976)
            sd.write_html('Device- 38.html', auto_open=True)

        elif self.n == 39 and self.z == 3:
            sd = no.read("C:/Users/noha.omar/Desktop/Govee1/yarb39_temp.csv",
                         "C:/Users/noha.omar/Desktop/Govee1/yarb39_hum.csv", "MAL 2 Outer Part", 2976)
            sd.write_html('Device- 39.html', auto_open=True)
        elif self.n == 40 and self.z == 3:
            sd = no.read("C:/Users/noha.omar/Desktop/Govee1/yarb40_temp.csv",
                         "C:/Users/noha.omar/Desktop/Govee1/yarb40_hum.csv", "Corridor Liquid First Floor", 2976)
            sd.write_html('Device- 40.html', auto_open=True)
        elif self.n == 41 and self.z == 3:
            sd = no.read("C:/Users/noha.omar/Desktop/Govee1/yarb41_temp.csv",
                         "C:/Users/noha.omar/Desktop/Govee1/yarb41_hum.csv", "SS2 Packaging Syrup", 2976)
            sd.write_html('Device- 41.html', auto_open=True)
        elif self.n == 42 and self.z == 3:
            sd = no.read("C:/Users/noha.omar/Desktop/Govee1/yarb42_temp.csv",
                         "C:/Users/noha.omar/Desktop/Govee1/yarb42_hum.csv", "Syrup Packaging EMA Safe", 2976)
            sd.write_html('Device- 42.html', auto_open=True)

        elif self.n == 43 and self.z == 3:
            sd = no.read("C:/Users/noha.omar/Desktop/Govee1/yarb43_temp.csv",
                         "C:/Users/noha.omar/Desktop/Govee1/yarb43_hum.csv", "Semisolid Filling 3", 2976)
            sd.write_html('Device- 43.html', auto_open=True)
        elif self.n == 44 and self.z == 3:
            sd = no.read("C:/Users/noha.omar/Desktop/Govee1/yarb44_temp.csv",
                         "C:/Users/noha.omar/Desktop/Govee1/yarb44_hum.csv", "Sk (Liq.Prep 2)", 2976)
            sd.write_html('Device- 44.html', auto_open=True)
        elif self.n == 45 and self.z == 3:
            sd = no.read("C:/Users/noha.omar/Desktop/Govee1/yarb45_temp.csv",
                         "C:/Users/noha.omar/Desktop/Govee1/yarb45_hum.csv", "Fryma Old (Cream Prep)", 2976)
            sd.write_html('Device- 45.html', auto_open=True)
        elif self.n == 46 and self.z == 3:
            sd = no.read("C:/Users/noha.omar/Desktop/Govee1/yarb46_temp.csv",
                         "C:/Users/noha.omar/Desktop/Govee1/yarb46_hum.csv", "Fryma New (Semisolid Prep)", 2976)
            sd.write_html('Device- 46.html', auto_open=True)
        elif self.n == 47 and self.z == 3:
            sd = no.read("C:/Users/noha.omar/Desktop/Govee1/yarb47_temp.csv",
                         "C:/Users/noha.omar/Desktop/Govee1/yarb47_hum.csv", "Liq . Prep 1(Old)", 2976)
            sd.write_html('Device- 47.html', auto_open=True)

        elif self.n == 48 and self.z == 3:
            sd = no.read("C:/Users/noha.omar/Desktop/Govee1/yarb48_temp.csv",
                         "C:/Users/noha.omar/Desktop/Govee1/yarb48_hum.csv", "Axomatic New (Semisolid Filling 2)", 2976)
            sd.write_html('Device- 48.html', auto_open=True)

        elif self.n == 49 and self.z == 3:
            sd = no.read("C:/Users/noha.omar/Desktop/Govee1/yarb49_temp.csv",
                         "C:/Users/noha.omar/Desktop/Govee1/yarb49_hum.csv", "Axomatic Old (Semisolid Filling 1)", 2976)
            sd.write_html('Device- 49.html', auto_open=True)
        elif self.n == 50 and self.z == 3:
            sd = no.read("C:/Users/noha.omar/Desktop/Govee1/yarb50_temp.csv",
                         "C:/Users/noha.omar/Desktop/Govee1/yarb50_hum.csv", "Ext. Prep Room", 2976)
            sd.write_html('Device- 50.html', auto_open=True)

        elif self.n == 51 and self.z == 3:
            sd = no.read("C:/Users/noha.omar/Desktop/Govee1/yarb51_temp.csv",
                         "C:/Users/noha.omar/Desktop/Govee1/yarb51_hum.csv", "Ext. Cleaning Line", 2976)
            sd.write_html('Device- 51.html', auto_open=True)
        elif self.n == 52 and self.z == 3:
            sd = no.read("C:/Users/noha.omar/Desktop/Govee1/yarb52_temp.csv",
                         "C:/Users/noha.omar/Desktop/Govee1/yarb52_hum.csv", "Ext. Filling Line", 2976)
            sd.write_html('Device- 52.html', auto_open=True)

        elif self.n == 53 and self.z == 3:
            sd = no.read("C:/Users/noha.omar/Desktop/Govee1/yarb53_temp.csv",
                         "C:/Users/noha.omar/Desktop/Govee1/yarb53_hum.csv", "Depaking Room for Liquid", 2976)
            sd.write_html('Device- 53.html', auto_open=True)
        elif self.n == 54 and self.z == 3:
            sd = no.read("C:/Users/noha.omar/Desktop/Govee1/yarb54_temp.csv",
                         "C:/Users/noha.omar/Desktop/Govee1/yarb54_hum.csv", "Corridor in Liquid area(2nd Floor)", 2976)
            sd.write_html('Device- 54.html', auto_open=True)
        elif self.n == 55 and self.z == 3:
            sd = no.read("C:/Users/noha.omar/Desktop/Govee1/yarb55_temp.csv",
                         "C:/Users/noha.omar/Desktop/Govee1/yarb55_hum.csv", "MAl Semisolid Inner Part", 2976)
            sd.write_html('Device- 55.html', auto_open=True)
        elif self.n == 56 and self.z == 3:
            sd = no.read("C:/Users/noha.omar/Desktop/Govee1/yarb56_temp.csv",
                         "C:/Users/noha.omar/Desktop/Govee1/yarb56_hum.csv", "MAl Semisolid Outer Part", 2976)
            sd.write_html('Device- 56.html', auto_open=True)
        elif self.n == 57 and self.z == 3:
            sd = no.read("C:/Users/noha.omar/Desktop/Govee1/yarb57_temp.csv",
                         "C:/Users/noha.omar/Desktop/Govee1/yarb57_hum.csv", "Partina (Blistering Room 1)", 2976)
            sd.write_html('Device- 57.html', auto_open=True)
        elif self.n == 58 and self.z == 3:
            sd = no.read("C:/Users/noha.omar/Desktop/Govee1/yarb58_temp.csv",
                         "C:/Users/noha.omar/Desktop/Govee1/yarb58_hum.csv", "Tablet Counter Room", 2976)
            sd.write_html('Device- 58.html', auto_open=True)
        elif self.n == 59 and self.z == 3:
            sd = no.read("C:/Users/noha.omar/Desktop/Govee1/yarb59_temp.csv",
                         "C:/Users/noha.omar/Desktop/Govee1/yarb59_hum.csv", "Pam New (Bilistering 3)", 2976)
            sd.write_html('Device- 59.html', auto_open=True)

        elif self.n == 60 and self.z == 3:
            sd = no.read("C:/Users/noha.omar/Desktop/Govee1/yarb60_temp.csv",
                         "C:/Users/noha.omar/Desktop/Govee1/yarb60_hum.csv", "Pam Old (Bilistering 2)", 2976)
            sd.write_html('Device- 60.html', auto_open=True)

        elif self.n == 61 and self.z == 3:
            sd = no.read("C:/Users/noha.omar/Desktop/Govee1/yarb61_temp.csv",
                         "C:/Users/noha.omar/Desktop/Govee1/yarb61_hum.csv", "MAL Bilistering ", 2976)
            sd.write_html('Device- 61.html', auto_open=True)
        elif self.n == 62 and self.z == 3:
            sd = no.read("C:/Users/noha.omar/Desktop/Govee1/yarb62_temp.csv",
                         "C:/Users/noha.omar/Desktop/Govee1/yarb62_hum.csv", " Bilistering  Corridor", 2976)
            sd.write_html('Device- 62.html', auto_open=True)

        elif self.n == 63 and self.z == 3:
            sd = no.read("C:/Users/noha.omar/Desktop/Govee1/yarb63_temp.csv",
                         "C:/Users/noha.omar/Desktop/Govee1/yarb63_hum.csv", " SS (Packaging Machine)", 2976)
            sd.write_html('Device- 63.html', auto_open=True)
        elif self.n == 64 and self.z == 3:
            sd = no.read("C:/Users/noha.omar/Desktop/Govee1/yarb64_temp.csv",
                         "C:/Users/noha.omar/Desktop/Govee1/yarb64_hum.csv", " Packaging Blister", 2976)
            sd.write_html('Device- 64.html', auto_open=True)

        elif self.n == 65 and self.z == 3:
            sd = no.read("C:/Users/noha.omar/Desktop/Govee1/yarb65_temp.csv",
                         "C:/Users/noha.omar/Desktop/Govee1/yarb65_hum.csv", " Pamphlet Area (Metronic Machine)", 2976)
            sd.write_html('Device- 65.html', auto_open=True)
        elif self.n == 66 and self.z == 3:
            sd = no.read("C:/Users/noha.omar/Desktop/Govee1/yarb66_temp.csv",
                         "C:/Users/noha.omar/Desktop/Govee1/yarb66_hum.csv", " Holding Room Packaging Area", 2976)
            sd.write_html('Device- 66.html', auto_open=True)

        elif self.n == 67 and self.z == 3:
            sd = no.read("C:/Users/noha.omar/Desktop/Govee1/yarb67_temp.csv",
                         "C:/Users/noha.omar/Desktop/Govee1/yarb67_hum.csv", " Weight Room 1", 2976)
            sd.write_html('Device- 67.html', auto_open=True)
        elif self.n == 68 and self.z == 3:
            sd = no.read("C:/Users/noha.omar/Desktop/Govee1/yarb68_temp.csv",
                         "C:/Users/noha.omar/Desktop/Govee1/yarb68_hum.csv", " Weight Room 2", 2976)
            sd.write_html('Device- 68.html', auto_open=True)
        elif self.n == 69 and self.z == 3:
            sd = no.read("C:/Users/noha.omar/Desktop/Govee1/yarb69_temp.csv",
                         "C:/Users/noha.omar/Desktop/Govee1/yarb69_hum.csv", " Weight Corridor", 2976)
            sd.write_html('Device- 69.html', auto_open=True)
        elif self.n == 70 and self.z == 3:
            sd = no.read("C:/Users/noha.omar/Desktop/Govee1/yarb70_temp.csv",
                         "C:/Users/noha.omar/Desktop/Govee1/yarb70_hum.csv", "Sampling", 2976)
            sd.write_html('Device- 70.html', auto_open=True)

        elif self.n == 71 and self.z == 3:
            sd = no.read("C:/Users/noha.omar/Desktop/Govee1/yarb71_temp.csv",
                         "C:/Users/noha.omar/Desktop/Govee1/yarb71_hum.csv", "QC Fridge", 2976)
            sd.write_html('Device- 71.html', auto_open=True)
        elif self.n == 72 and self.z == 3:
            sd = no.read("C:/Users/noha.omar/Desktop/Govee1/yarb72_temp.csv",
                         "C:/Users/noha.omar/Desktop/Govee1/yarb72_hum.csv", "QC Freezer", 2976)
            sd.write_html('Device- 72.html', auto_open=True)
        elif self.n == 73 and self.z == 3:
            sd = no.read("C:/Users/noha.omar/Desktop/Govee1/yarb73_temp.csv",
                         "C:/Users/noha.omar/Desktop/Govee1/yarb73_hum.csv", "Packaging (Pd Sticking Machine)", 2976)
            sd.write_html('Device- 73.html', auto_open=True)
        elif self.n == 74 and self.z == 3:
            sd = no.read("C:/Users/noha.omar/Desktop/Govee1/yarb74_temp.csv",
                         "C:/Users/noha.omar/Desktop/Govee1/yarb74_hum.csv", "CIP (2nd Floor)", 2976)
            sd.write_html('Device- 74.html', auto_open=True)
        elif self.n == 75 and self.z == 3:
            sd = no.read("C:/Users/noha.omar/Desktop/Govee1/yarb75_temp.csv",
                         "C:/Users/noha.omar/Desktop/Govee1/yarb75_hum.csv", "Cold Store", 2976)
            sd.write_html('Device- 75.html', auto_open=True)
        elif self.n == 76 and self.z == 3:
            sd = no.read("C:/Users/noha.omar/Desktop/Govee1/yarb76_temp.csv",
                         "C:/Users/noha.omar/Desktop/Govee1/yarb76_hum.csv", "Small Stability", 2976)
            sd.write_html('Device- 76.html', auto_open=True)
        elif self.n == 77 and self.z == 3:
            sd = no.read("C:/Users/noha.omar/Desktop/Govee1/yarb77_temp.csv",
                         "C:/Users/noha.omar/Desktop/Govee1/yarb77_hum.csv", "Large Stability", 2976)
            sd.write_html('Device- 77.html', auto_open=True)
        elif self.n == 78 and self.z == 3:
            sd = no.read("C:/Users/noha.omar/Desktop/Govee1/yarb78_temp.csv",
                         "C:/Users/noha.omar/Desktop/Govee1/yarb78_hum.csv", "R&D LAB", 2976)
            sd.write_html('Device- 78.html', auto_open=True)
        elif self.n == 79 and self.z == 3:
            sd = no.read("C:/Users/noha.omar/Desktop/Govee1/yarb79_temp.csv",
                         "C:/Users/noha.omar/Desktop/Govee1/yarb79_hum.csv", "R&D Fridge", 2976)
            sd.write_html('Device- 79.html', auto_open=True)
        elif self.n == 80 and self.z == 1:
            sd = no.read("C:/Users/noha.omar/Desktop/Govee1/yarb80_temp.csv",
                         "C:/Users/noha.omar/Desktop/Govee1/yarb80_hum.csv", "QC", 2976)
            sd.write_html('Device- 80.html', auto_open=True)
        elif self.n == 81 and self.z == 3:
            sd = no.read("C:/Users/noha.omar/Desktop/Govee1/yarb81_temp.csv",
                         "C:/Users/noha.omar/Desktop/Govee1/yarb81_hum.csv", "Cleaning room for liquid bottle 1(old)",
                         2976)
            sd.write_html('Device- 81.html', auto_open=True)
        elif self.n == 82 and self.z == 3:
            sd = no.read("C:/Users/noha.omar/Desktop/Govee1/yarb82_temp.csv",
                         "C:/Users/noha.omar/Desktop/Govee1/yarb82_hum.csv", "MAL 1 OUTER PART", 2976)
            sd.write_html('Device- 82.html', auto_open=True)
        elif self.n == 83 and self.z == 3:
            sd = no.read("C:/Users/noha.omar/Desktop/Govee1/yarb83_temp.csv",
                         "C:/Users/noha.omar/Desktop/Govee1/yarb83_hum.csv", "MAL 2 OUTER PART", 2976)
            sd.write_html('Device- 83.html', auto_open=True)
        elif self.n == 84 and self.z == 3:
            sd = no.read("C:/Users/noha.omar/Desktop/Govee1/yarb84_temp.csv",
                         "C:/Users/noha.omar/Desktop/Govee1/yarb84_hum.csv", "Clean Room Solid Area", 2976)
            sd.write_html('Device- 84.html', auto_open=True)
        elif self.n == 85 and self.z == 3:
            sd = no.read("C:/Users/noha.omar/Desktop/Govee1/yarb85_temp.csv",
                         "C:/Users/noha.omar/Desktop/Govee1/yarb85_hum.csv", "R&D Freezer", 2976)
            sd.write_html('Device- 85.html', auto_open=True)
        elif self.n == 86 and self.z == 3:
            sd = no.read("C:/Users/noha.omar/Desktop/Govee1/yarb86_temp.csv",
                         "C:/Users/noha.omar/Desktop/Govee1/yarb86_hum.csv", "R&D Lab2", 2976)
            sd.write_html('Device- 79.html', auto_open=True)
        elif self.n == 87 and self.z == 3:
            sd = no.read("C:/Users/noha.omar/Desktop/Govee1/yarb87_temp.csv",
                         "C:/Users/noha.omar/Desktop/Govee1/yarb87_hum.csv", "Incubator2", 2976)
            sd.write_html('Device- 87.html', auto_open=True)
        elif self.n == 88 and self.z == 3:
            sd = no.read("C:/Users/noha.omar/Desktop/Govee1/yarb88_temp.csv",
                         "C:/Users/noha.omar/Desktop/Govee1/yarb88_hum.csv", "Incubator1", 2976)
            sd.write_html('Device- 88.html', auto_open=True)
        elif self.n == 89 and self.z == 3:
            sd = no.read("C:/Users/noha.omar/Desktop/Govee1/yarb89_temp.csv",
                         "C:/Users/noha.omar/Desktop/Govee1/yarb89_hum.csv", "Incubator3", 2976)
            sd.write_html('Device- 89.html', auto_open=True)
        elif self.n == 90 and self.z == 3:
            sd = no.read("C:/Users/noha.omar/Desktop/Govee1/yarb90_temp.csv",
                         "C:/Users/noha.omar/Desktop/Govee1/yarb90_hum.csv", "Incubator4", 2976)
            sd.write_html('Device- 90.html', auto_open=True)
        elif self.n == 91 and self.z == 3:
            sd = no.read("C:/Users/noha.omar/Desktop/Govee1/yarb91_temp.csv",
                         "C:/Users/noha.omar/Desktop/Govee1/yarb91_hum.csv", "Micro fridge", 2976)
            sd.write_html('Device- 91.html', auto_open=True)
        elif self.n == 93 and self.z == 3:
            sd = no.read("C:/Users/noha.omar/Desktop/Govee1/yarb93_temp.csv",
                         "C:/Users/noha.omar/Desktop/Govee1/yarb93_hum.csv", "Weighting Room 2", 2976)
            sd.write_html('Device- 93.html', auto_open=True)
        elif self.n == 94 and self.z == 3:
            sd = no.read("C:/Users/noha.omar/Desktop/Govee1/yarb94_temp.csv",
                         "C:/Users/noha.omar/Desktop/Govee1/yarb94_hum.csv", "Retained Room 2", 2976)
            sd.write_html('Device- 94.html', auto_open=True)
        elif self.n == 95 and self.z == 3:
            sd = no.read("C:/Users/noha.omar/Desktop/Govee1/yarb95_temp.csv",
                         "C:/Users/noha.omar/Desktop/Govee1/yarb95_hum.csv", "Clean Liquid Level2", 2976)
            sd.write_html('Device- 95.html', auto_open=True)
        elif self.n == 96 and self.z == 3:
            sd = no.read("C:/Users/noha.omar/Desktop/Govee1/yarb96_temp.csv",
                         "C:/Users/noha.omar/Desktop/Govee1/yarb96_hum.csv", "Retained Room 1", 2976)
            sd.write_html('Device- 95.html', auto_open=True)
        elif self.n == 97 and self.z == 3:
            sd = no.read("C:/Users/noha.omar/Desktop/Govee1/yarb97_temp.csv",
                         "C:/Users/noha.omar/Desktop/Govee1/yarb97_hum.csv", "Store Cold spot", 2976)
            sd.write_html('Device- 95.html', auto_open=True)
        elif self.n == 98 and self.z == 3:
            sd = no.read("C:/Users/noha.omar/Desktop/Govee1/yarb98_temp.csv",
                         "C:/Users/noha.omar/Desktop/Govee1/yarb98_hum.csv", "Store hot spot", 2976)
            sd.write_html('Device- 95.html', auto_open=True)

            # years

        elif self.n == 1 and self.z == 4:
            sd = no.read("C:/Users/noha.omar/Desktop/Govee1/yarb1_temp.csv",
                         "C:/Users/noha.omar/Desktop/Govee1/yarb1_hum.csv", "Seive", 35712)
            sd.write_html('Device- 1.html', auto_open=True)
        elif self.n == 2 and self.z == 4:
            sd = no.read("C:/Users/noha.omar/Desktop/Govee1/yarb2_temp.csv",
                         "C:/Users/noha.omar/Desktop/Govee1/yarb2_hum.csv", "V Shape", 35712)
            sd.write_html('Device- 2.html', auto_open=True)
        elif self.n == 3 and self.z == 4:
            sd = no.read("C:/Users/noha.omar/Desktop/Govee1/yarb3_temp.csv",
                         "C:/Users/noha.omar/Desktop/Govee1/yarb3_hum.csv", "Small Coating", 35712)
            sd.write_html('Device- 3.html', auto_open=True)
        elif self.n == 4 and self.z == 4:
            sd = no.read("C:/Users/noha.omar/Desktop/Govee1/yarb4_temp.csv",
                         "C:/Users/noha.omar/Desktop/Govee1/yarb4_hum.csv", "Holding Room", 35712)
            sd.write_html('Device- 4.html', auto_open=True)
        elif self.n == 5 and self.z == 4:
            sd = no.read("C:/Users/noha.omar/Desktop/Govee1/yarb5_temp.csv",
                         "C:/Users/noha.omar/Desktop/Govee1/yarb5_hum.csv", "Coating Gansons(Room2)", 35712)
            sd.write_html('Device- 5.html', auto_open=True)
        elif self.n == 6 and self.z == 4:
            sd = no.read("C:/Users/noha.omar/Desktop/Govee1/yarb6_temp.csv",
                         "C:/Users/noha.omar/Desktop/Govee1/yarb6_hum.csv", "Sachet Filling2", 35712)
            sd.write_html('Device- 6 .html', auto_open=True)
        elif self.n == 7 and self.z == 4:
            sd = no.read("C:/Users/noha.omar/Desktop/Govee1/yarb7_temp.csv",
                         "C:/Users/noha.omar/Desktop/Govee1/yarb7_hum.csv", "Pilot(R&D Granulation)", 35712)
            sd.write_html('Device- 7.html', auto_open=True)
        elif self.n == 8 and self.z == 4:
            sd = no.read("C:/Users/noha.omar/Desktop/Govee1/yarb8_temp.csv",
                         "C:/Users/noha.omar/Desktop/Govee1/yarb8_hum.csv", "R&D Blinding", 35712)
            sd.write_html('Device- 8.html', auto_open=True)
        elif self.n == 9 and self.z == 4:
            sd = no.read("C:/Users/noha.omar/Desktop/Govee1/yarb9_temp.csv",
                         "C:/Users/noha.omar/Desktop/Govee1/yarb9_hum.csv", "R&D Compression", 35712)
            sd.write_html('Device- 9.html', auto_open=True)
        elif self.n == 10 and self.z == 4:
            sd = no.read("C:/Users/noha.omar/Desktop/Govee1/yarb10_temp.csv",
                         "C:/Users/noha.omar/Desktop/Govee1/yarb10_hum.csv", "Holding Room (028P1)(Middle)", 35712)
            sd.write_html('Device- 10.html', auto_open=True)



        elif self.n == 11 and self.z == 4:
            sd = no.read("C:/Users/noha.omar/Desktop/Govee1/yarb11_temp.csv",
                         "C:/Users/noha.omar/Desktop/Govee1/yarb11_hum.csv", "Capsule FillinG(Old)", 35712)
            sd.write_html('Device- 11.html', auto_open=True)

        elif self.n == 12 and self.z == 4:
            sd = no.read("C:/Users/noha.omar/Desktop/Govee1/yarb12_temp.csv",
                         "C:/Users/noha.omar/Desktop/Govee1/yarb12_hum.csv", "Compresstion Room1", 35712)
            sd.write_html('Device- 12.html', auto_open=True)
        elif self.n == 13 and self.z == 4:
            sd = no.read("C:/Users/noha.omar/Desktop/Govee1/yarb13_temp.csv",
                         "C:/Users/noha.omar/Desktop/Govee1/yarb13_hum.csv", "Granulation", 35712)
            sd.write_html('Device- 13.html', auto_open=True)
        elif self.n == 14 and self.z == 4:
            sd = no.read("C:/Users/noha.omar/Desktop/Govee1/yarb14_temp.csv",
                         "C:/Users/noha.omar/Desktop/Govee1/yarb14_hum.csv", "Bin Blender", 35712)
            sd.write_html('Device- 14.html', auto_open=True)
        elif self.n == 15 and self.z == 4:
            sd = no.read("C:/Users/noha.omar/Desktop/Govee1/yarb15_temp.csv",
                         "C:/Users/noha.omar/Desktop/Govee1/yarb15_hum.csv", "Compresstion Room2", 35712)
            sd.write_html('Device- 15.html', auto_open=True)
        elif self.n == 16 and self.z == 4:
            sd = no.read("C:/Users/noha.omar/Desktop/Govee1/yarb16_temp.csv",
                         "C:/Users/noha.omar/Desktop/Govee1/yarb16_hum.csv", "Granulation", 35712)
            sd.write_html('Device- 16.html', auto_open=True)

        elif self.n == 20 and self.z == 4:
            sd = no.read("C:/Users/noha.omar/Desktop/Govee1/yarb20_temp.csv",
                         "C:/Users/noha.omar/Desktop/Govee1/yarb20_hum.csv", "Depaking Room For Solid", 35712)
            sd.write_html('Device- 20.html', auto_open=True)

        elif self.n == 21 and self.z == 4:
            sd = no.read("C:/Users/noha.omar/Desktop/Govee1/yarb21_temp.csv",
                         "C:/Users/noha.omar/Desktop/Govee1/yarb21_hum.csv", "Bottle Clean For Dry Syrup", 35712)
            sd.write_html('Device- 21.html', auto_open=True)

        elif self.n == 22 and self.z == 4:
            sd = no.read("C:/Users/noha.omar/Desktop/Govee1/yarb22_temp.csv",
                         "C:/Users/noha.omar/Desktop/Govee1/yarb22_hum.csv", " Dry Syrup Filling", 35712)
            sd.write_html('Device- 22.html', auto_open=True)

        elif self.n == 23 and self.z == 4:
            sd = no.read("C:/Users/noha.omar/Desktop/Govee1/yarb23_temp.csv",
                         "C:/Users/noha.omar/Desktop/Govee1/yarb23_hum.csv", "Sachet Filling(Old)", 35712)
            sd.write_html('Device- 23.html', auto_open=True)

        elif self.n == 24 and self.z == 4:
            sd = no.read("C:/Users/noha.omar/Desktop/Govee1/yarb24_temp.csv",
                         "C:/Users/noha.omar/Desktop/Govee1/yarb24_hum.csv", "Coating Solution Prep ", 35712)
            sd.write_html('Device- 24.html', auto_open=True)

        elif self.n == 25 and self.z == 4:
            sd = no.read("C:/Users/noha.omar/Desktop/Govee1/yarb25_temp.csv",
                         "C:/Users/noha.omar/Desktop/Govee1/yarb25_hum.csv", "Capsule Filling 2 ", 35712)
            sd.write_html('Device- 25.html', auto_open=True)


        elif self.n == 26 and self.z == 4:
            sd = no.read("C:/Users/noha.omar/Desktop/Govee1/yarb26_temp.csv",
                         "C:/Users/noha.omar/Desktop/Govee1/yarb26_hum.csv", "Coating Room 1(Old) ", 35712)
            sd.write_html('Device- 26 .html', auto_open=True)
        elif self.n == 27 and self.z == 4:
            sd = no.read("C:/Users/noha.omar/Desktop/Govee1/yarb27_temp.csv",
                         "C:/Users/noha.omar/Desktop/Govee1/yarb27_hum.csv", "Corridor Against  sacchet Filling ", 35712)
            sd.write_html('Device- 27.html', auto_open=True)
        elif self.n == 28 and self.z == 4:
            sd = no.read("C:/Users/noha.omar/Desktop/Govee1/yarb28_temp.csv",
                         "C:/Users/noha.omar/Desktop/Govee1/yarb28_hum.csv", "Corridor Against V Shape ", 35712)
            sd.write_html('Device- 18.html', auto_open=True)
        elif self.n == 29 and self.z == 4:
            sd = no.read("C:/Users/noha.omar/Desktop/Govee1/yarb29_temp.csv",
                         "C:/Users/noha.omar/Desktop/Govee1/yarb29_hum.csv", "Stage Out (Solid area)", 35712)
            sd.write_html('Device- 29.html', auto_open=True)
        elif self.n == 30 and self.z == 4:
            sd = no.read("C:/Users/noha.omar/Desktop/Govee1/yarb30_temp.csv",
                         "C:/Users/noha.omar/Desktop/Govee1/yarb30_hum.csv", "Corridor Against IPC ", 35712)
            sd.write_html('Device- 30.html', auto_open=True)
        elif self.n == 31 and self.z == 4:
            sd = no.read("C:/Users/noha.omar/Desktop/Govee1/yarb31_temp.csv",
                         "C:/Users/noha.omar/Desktop/Govee1/yarb31_hum.csv", "MAl (Solid area)", 35712)
            sd.write_html('Device- 31.html', auto_open=True)

        elif self.n == 32 and self.z == 4:
            sd = no.read("C:/Users/noha.omar/Desktop/Govee1/yarb32_temp.csv",
                         "C:/Users/noha.omar/Desktop/Govee1/yarb32_hum.csv", "Cleaning Room for Liquid bottle1(Old)",
                         35712)
            sd.write_html('Device- 32.html', auto_open=True)

        elif self.n == 33 and self.z == 4:
            sd = no.read("C:/Users/noha.omar/Desktop/Govee1/yarb33_temp.csv",
                         "C:/Users/noha.omar/Desktop/Govee1/yarb33_hum.csv", "Filling Room for Liquid 1(Old)", 35712)
            sd.write_html('Device- 33.html', auto_open=True)
        elif self.n == 34 and self.z == 4:
            sd = no.read("C:/Users/noha.omar/Desktop/Govee1/yarb34_temp.csv",
                         "C:/Users/noha.omar/Desktop/Govee1/yarb34_hum.csv", "Cleaning Room for Liquid bottle2(new)",
                         35712)
            sd.write_html('Device- 34.html', auto_open=True)
        elif self.n == 35 and self.z == 4:
            sd = no.read("C:/Users/noha.omar/Desktop/Govee1/yarb35_temp.csv",
                         "C:/Users/noha.omar/Desktop/Govee1/yarb35_hum.csv", "Filling Room for Liquid 2(new)", 35712)
            sd.write_html('Device- 35.html', auto_open=True)
        elif self.n == 36 and self.z == 4:
            sd = no.read("C:/Users/noha.omar/Desktop/Govee1/yarb36_temp.csv",
                         "C:/Users/noha.omar/Desktop/Govee1/yarb36_hum.csv", "MAL 1 Inner Part", 35712)
            sd.write_html('Device- 36.html', auto_open=True)
        elif self.n == 37 and self.z == 4:
            sd = no.read("C:/Users/noha.omar/Desktop/Govee1/yarb37_temp.csv",
                         "C:/Users/noha.omar/Desktop/Govee1/yarb37_hum.csv", "MAL 1 Outer Part", 35712)
            sd.write_html('Device- 37 .html', auto_open=True)
        elif self.n == 38 and self.z == 4:
            sd = no.read("C:/Users/noha.omar/Desktop/Govee1/yarb38_temp.csv",
                         "C:/Users/noha.omar/Desktop/Govee1/yarb38_hum.csv", "MAL 2 Inner Part", 35712)
            sd.write_html('Device- 38.html', auto_open=True)
        elif self.n == 39 and self.z == 4:
            sd = no.read("C:/Users/noha.omar/Desktop/Govee1/yarb39_temp.csv",
                         "C:/Users/noha.omar/Desktop/Govee1/yarb39_hum.csv", "MAL 2 Outer Part", 35712)
            sd.write_html('Device- 39.html', auto_open=True)
        elif self.n == 40 and self.z == 4:
            sd = no.read("C:/Users/noha.omar/Desktop/Govee1/yarb40_temp.csv",
                         "C:/Users/noha.omar/Desktop/Govee1/yarb40_hum.csv", "Corridor Liquid First Floor", 35712)
            sd.write_html('Device- 40.html', auto_open=True)
        elif self.n == 41 and self.z == 4:
            sd = no.read("C:/Users/noha.omar/Desktop/Govee1/yarb41_temp.csv",
                         "C:/Users/noha.omar/Desktop/Govee1/yarb41_hum.csv", "SS2 Packaging Syrup", 35712)
            sd.write_html('Device- 41.html', auto_open=True)
        elif self.n == 42 and self.z == 4:
            sd = no.read("C:/Users/noha.omar/Desktop/Govee1/yarb42_temp.csv",
                         "C:/Users/noha.omar/Desktop/Govee1/yarb42_hum.csv", "Syrup Packaging EMA Safe", 35712)
            sd.write_html('Device- 42.html', auto_open=True)
        elif self.n == 43 and self.z == 4:
            sd = no.read("C:/Users/noha.omar/Desktop/Govee1/yarb43_temp.csv",
                         "C:/Users/noha.omar/Desktop/Govee1/yarb43_hum.csv", "Semisolid Filling 3", 35712)
            sd.write_html('Device- 43.html', auto_open=True)

        elif self.n == 44 and self.z == 4:
            sd = no.read("C:/Users/noha.omar/Desktop/Govee1/yarb44_temp.csv",
                         "C:/Users/noha.omar/Desktop/Govee1/yarb44_hum.csv", "Sk (Liq.Prep 2)", 35712)
            sd.write_html('Device- 44.html', auto_open=True)

        elif self.n == 45 and self.z == 4:
            sd = no.read("C:/Users/noha.omar/Desktop/Govee1/yarb45_temp.csv",
                         "C:/Users/noha.omar/Desktop/Govee1/yarb45_hum.csv", "Fryma Old (Cream Prep)", 35712)
            sd.write_html('Device- 45.html', auto_open=True)
        elif self.n == 46 and self.z == 4:
            sd = no.read("C:/Users/noha.omar/Desktop/Govee1/yarb46_temp.csv",
                         "C:/Users/noha.omar/Desktop/Govee1/yarb46_hum.csv", "Fryma New (Semisolid Prep)", 35712)
            sd.write_html('Device- 46.html', auto_open=True)
        elif self.n == 47 and self.z == 4:
            sd = no.read("C:/Users/noha.omar/Desktop/Govee1/yarb47_temp.csv",
                         "C:/Users/noha.omar/Desktop/Govee1/yarb47_hum.csv", "Liq . Prep 1(Old)", 35712)
            sd.write_html('Device- 47.html', auto_open=True)
        elif self.n == 48 and self.z == 4:
            sd = no.read("C:/Users/noha.omar/Desktop/Govee1/yarb48_temp.csv",
                         "C:/Users/noha.omar/Desktop/Govee1/yarb48_hum.csv", "Axomatic New (Semisolid Filling 2)", 35712)
            sd.write_html('Device- 48.html', auto_open=True)
        elif self.n == 49 and self.z == 4:
            sd = no.read("C:/Users/noha.omar/Desktop/Govee1/yarb49_temp.csv",
                         "C:/Users/noha.omar/Desktop/Govee1/yarb49_hum.csv", "Axomatic Old (Semisolid Filling 1)", 35712)
            sd.write_html('Device- 49.html', auto_open=True)
        elif self.n == 50 and self.z == 4:
            sd = no.read("C:/Users/noha.omar/Desktop/Govee1/yarb50_temp.csv",
                         "C:/Users/noha.omar/Desktop/Govee1/yarb50_hum.csv", "Ext. Prep Room", 35712)
            sd.write_html('Device- 50.html', auto_open=True)
        elif self.n == 51 and self.z == 4:
            sd = no.read("C:/Users/noha.omar/Desktop/Govee1/yarb51_temp.csv",
                         "C:/Users/noha.omar/Desktop/Govee1/yarb51_hum.csv", "Ext. Cleaning Line", 35712)
            sd.write_html('Device- 51.html', auto_open=True)
        elif self.n == 52 and self.z == 4:
            sd = no.read("C:/Users/noha.omar/Desktop/Govee1/yarb52_temp.csv",
                         "C:/Users/noha.omar/Desktop/Govee1/yarb52_hum.csv", "Ext. Filling Line", 35712)
            sd.write_html('Device- 52.html', auto_open=True)
        elif self.n == 53 and self.z == 4:
            sd = no.read("C:/Users/noha.omar/Desktop/Govee1/yarb53_temp.csv",
                         "C:/Users/noha.omar/Desktop/Govee1/yarb53_hum.csv", "Depaking Room for Liquid", 35712)
            sd.write_html('Device- 53.html', auto_open=True)

        elif self.n == 54 and self.z == 4:
            sd = no.read("C:/Users/noha.omar/Desktop/Govee1/yarb54_temp.csv",
                         "C:/Users/noha.omar/Desktop/Govee1/yarb54_hum.csv", "Corridor in Liquid area(2nd Floor)", 35712)
            sd.write_html('Device- 54.html', auto_open=True)
        elif self.n == 55 and self.z == 4:
            sd = no.read("C:/Users/noha.omar/Desktop/Govee1/yarb55_temp.csv",
                         "C:/Users/noha.omar/Desktop/Govee1/yarb55_hum.csv", "MAl Semisolid Inner Part", 35712)
            sd.write_html('Device- 55.html', auto_open=True)
        elif self.n == 56 and self.z == 4:
            sd = no.read("C:/Users/noha.omar/Desktop/Govee1/yarb56_temp.csv",
                         "C:/Users/noha.omar/Desktop/Govee1/yarb56_hum.csv", "MAl Semisolid Outer Part", 35712)
            sd.write_html('Device- 56.html', auto_open=True)

        elif self.n == 57 and self.z == 4:
            sd = no.read("C:/Users/noha.omar/Desktop/Govee1/yarb57_temp.csv",
                         "C:/Users/noha.omar/Desktop/Govee1/yarb57_hum.csv", "Partina (Blistering Room 1)", 35712)
            sd.write_html('Device- 57.html', auto_open=True)
        elif self.n == 58 and self.z == 4:
            sd = no.read("C:/Users/noha.omar/Desktop/Govee1/yarb58_temp.csv",
                         "C:/Users/noha.omar/Desktop/Govee1/yarb58_hum.csv", "Tablet Counter Room", 35712)
            sd.write_html('Device- 58.html', auto_open=True)
        elif self.n == 59 and self.z == 4:
            sd = no.read("C:/Users/noha.omar/Desktop/Govee1/yarb59_temp.csv",
                         "C:/Users/noha.omar/Desktop/Govee1/yarb59_hum.csv", "Pam New (Bilistering 3)", 35712)
            sd.write_html('Device- 59.html', auto_open=True)
        elif self.n == 60 and self.z == 4:
            sd = no.read("C:/Users/noha.omar/Desktop/Govee1/yarb60_temp.csv",
                         "C:/Users/noha.omar/Desktop/Govee1/yarb60_hum.csv", "Pam Old (Bilistering 2)", 35712)
            sd.write_html('Device- 60.html', auto_open=True)
        elif self.n == 61 and self.z == 4:
            sd = no.read("C:/Users/noha.omar/Desktop/Govee1/yarb61_temp.csv",
                         "C:/Users/noha.omar/Desktop/Govee1/yarb61_hum.csv", "MAL Bilistering ", 35712)
            sd.write_html('Device- 61 .html', auto_open=True)
        elif self.n == 62 and self.z == 4:
            sd = no.read("C:/Users/noha.omar/Desktop/Govee1/yarb62_temp.csv",
                         "C:/Users/noha.omar/Desktop/Govee1/yarb62_hum.csv", " Bilistering  Corridor", 35712)
            sd.write_html('Device- 62.html', auto_open=True)
        elif self.n == 63 and self.z == 4:
            sd = no.read("C:/Users/noha.omar/Desktop/Govee1/yarb63_temp.csv",
                         "C:/Users/noha.omar/Desktop/Govee1/yarb63_hum.csv", " SS (Packaging Machine)", 35712)
            sd.write_html('Device- 63.html', auto_open=True)
        elif self.n == 64 and self.z == 4:
            sd = no.read("C:/Users/noha.omar/Desktop/Govee1/yarb64_temp.csv",
                         "C:/Users/noha.omar/Desktop/Govee1/yarb64_hum.csv", " Packaging Blister", 35712)
            sd.write_html('Device- 64.html', auto_open=True)
        elif self.n == 65 and self.z == 4:
            sd = no.read("C:/Users/noha.omar/Desktop/Govee1/yarb65_temp.csv",
                         "C:/Users/noha.omar/Desktop/Govee1/yarb65_hum.csv", " Pamphlet Area (Metronic Machine)", 35712)
            sd.write_html('Device- 65.html', auto_open=True)

        elif self.n == 66 and self.z == 4:
            sd = no.read("C:/Users/noha.omar/Desktop/Govee1/yarb66_temp.csv",
                         "C:/Users/noha.omar/Desktop/Govee1/yarb66_hum.csv", " Holding Room Packaging Area", 35712)
            sd.write_html('Device- 66.html', auto_open=True)

        elif self.n == 67 and self.z == 4:
            sd = no.read("C:/Users/noha.omar/Desktop/Govee1/yarb67_temp.csv",
                         "C:/Users/noha.omar/Desktop/Govee1/yarb67_hum.csv", " Weight Room 1", 35712)
            sd.write_html('Device- 67.html', auto_open=True)
        elif self.n == 68 and self.z == 4:
            sd = no.read("C:/Users/noha.omar/Desktop/Govee1/yarb68_temp.csv",
                         "C:/Users/noha.omar/Desktop/Govee1/yarb68_hum.csv", " Weight Room 2", 35712)
            sd.write_html('Device- 68.html', auto_open=True)
        elif self.n == 69 and self.z == 4:
            sd = no.read("C:/Users/noha.omar/Desktop/Govee1/yarb69_temp.csv",
                         "C:/Users/noha.omar/Desktop/Govee1/yarb69_hum.csv", " Weight Corridor", 35712)
            sd.write_html('Device- 69.html', auto_open=True)
        elif self.n == 70 and self.z == 4:
            sd = no.read("C:/Users/noha.omar/Desktop/Govee1/yarb70_temp.csv",
                         "C:/Users/noha.omar/Desktop/Govee1/yarb70_hum.csv", "Sampling", 35712)
            sd.write_html('Device- 70.html', auto_open=True)
        elif self.n == 71 and self.z == 4:
            sd = no.read("C:/Users/noha.omar/Desktop/Govee1/yarb71_temp.csv",
                         "C:/Users/noha.omar/Desktop/Govee1/yarb71_hum.csv", "QC Fridge", 35712)
            sd.write_html('Device- 71.html', auto_open=True)

        elif self.n == 72 and self.z == 4:
            sd = no.read("C:/Users/noha.omar/Desktop/Govee1/yarb72_temp.csv",
                         "C:/Users/noha.omar/Desktop/Govee1/yarb72_hum.csv", "QC Freezer", 35712)
            sd.write_html('Device- 72.html', auto_open=True)
        elif self.n == 73 and self.z == 4:
            sd = no.read("C:/Users/noha.omar/Desktop/Govee1/yarb73_temp.csv",
                         "C:/Users/noha.omar/Desktop/Govee1/yarb73_hum.csv", "Packaging (Pd Sticking Machine)", 35712)
            sd.write_html('Device- 73.html', auto_open=True)
        elif self.n == 74 and self.z == 4:
            sd = no.read("C:/Users/noha.omar/Desktop/Govee1/yarb74_temp.csv",
                         "C:/Users/noha.omar/Desktop/Govee1/yarb74_hum.csv", "CIP (2nd Floor)", 35712)
            sd.write_html('Device- 74.html', auto_open=True)
        elif self.n == 75 and self.z == 4:
            sd = no.read("C:/Users/noha.omar/Desktop/Govee1/yarb75_temp.csv",
                         "C:/Users/noha.omar/Desktop/Govee1/yarb75_hum.csv", "Cold Store", 35712)
            sd.write_html('Device- 75.html', auto_open=True)
        elif self.n == 76 and self.z == 4:
            sd = no.read("C:/Users/noha.omar/Desktop/Govee1/yarb76_temp.csv",
                         "C:/Users/noha.omar/Desktop/Govee1/yarb76_hum.csv", "Small Stability", 35712)
            sd.write_html('Device- 76.html', auto_open=True)
        elif self.n == 77 and self.z == 4:
            sd = no.read("C:/Users/noha.omar/Desktop/Govee1/yarb77_temp.csv",
                         "C:/Users/noha.omar/Desktop/Govee1/yarb77_hum.csv", "Large Stability", 35712)
            sd.write_html('Device- 77.html', auto_open=True)
        elif self.n == 78 and self.z == 4:
            sd = no.read("C:/Users/noha.omar/Desktop/Govee1/yarb78_temp.csv",
                         "C:/Users/noha.omar/Desktop/Govee1/yarb78_hum.csv", "R&D LAB", 35712)
            sd.write_html('Device- 78.html', auto_open=True)
        elif self.n == 79 and self.z == 4:
            sd = no.read("C:/Users/noha.omar/Desktop/Govee1/yarb79_temp.csv",
                         "C:/Users/noha.omar/Desktop/Govee1/yarb79_hum.csv", "R&D Fridge", 35712)
            sd.write_html('Device- 79.html', auto_open=True)
        elif self.n == 80 and self.z == 1:
            sd = no.read("C:/Users/noha.omar/Desktop/Govee1/yarb80_temp.csv",
                         "C:/Users/noha.omar/Desktop/Govee1/yarb80_hum.csv", "QC", 35712)
            sd.write_html('Device- 80.html', auto_open=True)

        elif self.n == 81 and self.z == 4:
            sd = no.read("C:/Users/noha.omar/Desktop/Govee1/yarb81_temp.csv",
                         "C:/Users/noha.omar/Desktop/Govee1/yarb81_hum.csv", "Cleaning room for liquid bottle 1(old)",
                         35712)
            sd.write_html('Device- 81.html', auto_open=True)
        elif self.n == 82 and self.z == 4:
            sd = no.read("C:/Users/noha.omar/Desktop/Govee1/yarb82_temp.csv",
                         "C:/Users/noha.omar/Desktop/Govee1/yarb82_hum.csv", "MAL 1 OUTER PART", 35712)
            sd.write_html('Device- 82.html', auto_open=True)
        elif self.n == 83 and self.z == 4:
            sd = no.read("C:/Users/noha.omar/Desktop/Govee1/yarb83_temp.csv",
                         "C:/Users/noha.omar/Desktop/Govee1/yarb83_hum.csv", "MAL 2 OUTER PART", 35712)
            sd.write_html('Device- 83.html', auto_open=True)
        elif self.n == 84 and self.z == 4:
            sd = no.read("C:/Users/noha.omar/Desktop/Govee1/yarb84_temp.csv",
                         "C:/Users/noha.omar/Desktop/Govee1/yarb84_hum.csv", "Clean Room Solid Area", 35712)
            sd.write_html('Device- 84.html', auto_open=True)
        elif self.n == 85 and self.z == 4:
            sd = no.read("C:/Users/noha.omar/Desktop/Govee1/yarb85_temp.csv",
                         "C:/Users/noha.omar/Desktop/Govee1/yarb85_hum.csv", "R&D Freezer", 35712)
            sd.write_html('Device- 85.html', auto_open=True)
        elif self.n == 86 and self.z == 4:
            sd = no.read("C:/Users/noha.omar/Desktop/Govee1/yarb86_temp.csv",
                         "C:/Users/noha.omar/Desktop/Govee1/yarb86_hum.csv", "R&D Lab2", 35712)
            sd.write_html('Device- 79.html', auto_open=True)
        elif self.n == 87 and self.z == 4:
            sd = no.read("C:/Users/noha.omar/Desktop/Govee1/yarb87_temp.csv",
                         "C:/Users/noha.omar/Desktop/Govee1/yarb87_hum.csv", "Incubator2", 35712)
            sd.write_html('Device- 87.html', auto_open=True)
        elif self.n == 88 and self.z == 4:
            sd = no.read("C:/Users/noha.omar/Desktop/Govee1/yarb88_temp.csv",
                         "C:/Users/noha.omar/Desktop/Govee1/yarb88_hum.csv", "Incubator1", 35712)
            sd.write_html('Device- 88.html', auto_open=True)
        elif self.n == 89 and self.z == 4:
            sd = no.read("C:/Users/noha.omar/Desktop/Govee1/yarb89_temp.csv",
                         "C:/Users/noha.omar/Desktop/Govee1/yarb89_hum.csv", "Incubator3", 35712)
            sd.write_html('Device- 89.html', auto_open=True)
        elif self.n == 90 and self.z == 4:
            sd = no.read("C:/Users/noha.omar/Desktop/Govee1/yarb90_temp.csv",
                         "C:/Users/noha.omar/Desktop/Govee1/yarb90_hum.csv", "Incubator4", 35712)
            sd.write_html('Device- 90.html', auto_open=True)
        elif self.n == 91 and self.z == 4:
            sd = no.read("C:/Users/noha.omar/Desktop/Govee1/yarb91_temp.csv",
                         "C:/Users/noha.omar/Desktop/Govee1/yarb91_hum.csv", "Micro fridge", 35712)
            sd.write_html('Device- 91.html', auto_open=True)
        elif self.n == 93 and self.z == 4:
            sd = no.read("C:/Users/noha.omar/Desktop/Govee1/yarb93_temp.csv",
                         "C:/Users/noha.omar/Desktop/Govee1/yarb93_hum.csv", "Weighting Room 2", 35712)
            sd.write_html('Device- 93.html', auto_open=True)
        elif self.n == 94 and self.z == 4:
            sd = no.read("C:/Users/noha.omar/Desktop/Govee1/yarb94_temp.csv",
                         "C:/Users/noha.omar/Desktop/Govee1/yarb94_hum.csv", "Retained Room 2", 35712)
            sd.write_html('Device- 94.html', auto_open=True)
        elif self.n == 95 and self.z == 4:
            sd = no.read("C:/Users/noha.omar/Desktop/Govee1/yarb95_temp.csv",
                         "C:/Users/noha.omar/Desktop/Govee1/yarb95_hum.csv", "Clean Liquid Level2", 35712)
            sd.write_html('Device- 95.html', auto_open=True)
        elif self.n == 96 and self.z == 4:
            sd = no.read("C:/Users/noha.omar/Desktop/Govee1/yarb96_temp.csv",
                         "C:/Users/noha.omar/Desktop/Govee1/yarb96_hum.csv", "Retained Room 1", 35712)
            sd.write_html('Device- 95.html', auto_open=True)
        elif self.n == 97 and self.z == 4:
            sd = no.read("C:/Users/noha.omar/Desktop/Govee1/yarb97_temp.csv",
                         "C:/Users/noha.omar/Desktop/Govee1/yarb97_hum.csv", "Store Cold spot", 35712)
            sd.write_html('Device- 95.html', auto_open=True)
        elif self.n == 98 and self.z == 4:
            sd = no.read("C:/Users/noha.omar/Desktop/Govee1/yarb98_temp.csv",
                         "C:/Users/noha.omar/Desktop/Govee1/yarb98_hum.csv", "Store hot spot", 35712)
            sd.write_html('Device- 95.html', auto_open=True)


# x = no(1,1)
# x.yarb5()
