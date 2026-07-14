import flet as ft
import data  # data.py ကနေ offers ကို ယူမယ်

def main(page: ft.Page):
    page.title = "Barmill Offer - Spare Parts"
    page.scroll = ft.ScrollMode.ADAPTIVE
    page.padding = 15
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

    # ခေါင်းစီး
    header = ft.Text("🛠️ Barmill Offer - အစိတ်အပိုင်းစာရင်း", size=24, weight=ft.FontWeight.BOLD)

    # ดေတာကို Table နဲ့ပြမယ်
    if not hasattr(data, 'offers') or not data.offers:
        content = ft.Text("Excel ဖိုင်မရှိပါ သို့မဟုတ် ဒေတာဗလာဖြစ်နေသည်။", size=16, color=ft.colors.RED_700)
    else:
        # Table columns သတ်မှတ်ခြင်း
        columns = [
            ft.DataColumn(ft.Text("No.", weight=ft.FontWeight.BOLD)),
            ft.DataColumn(ft.Text("Item", weight=ft.FontWeight.BOLD)),
            ft.DataColumn(ft.Text("Code", weight=ft.FontWeight.BOLD)),
            ft.DataColumn(ft.Text("Drawing No.", weight=ft.FontWeight.BOLD)),
            ft.DataColumn(ft.Text("Price (USD)", weight=ft.FontWeight.BOLD)),
        ]

        rows = []
        for item in data.offers[:100]:  # ပထမ ၁၀၀ ခုပဲပြမည်
            # Key နာမည်တွင် \n ပါသည်ဖြစ်စေ၊ မပါသည်ဖြစ်စေ ဖတ်နိုင်ရန် ပြင်ဆင်ခြင်း
            price_val = item.get("Unit Price (USD)") or item.get("Unit Price\n(USD)") or ""
            drawing_val = item.get("96/3805 Drawing no.") or item.get("96/3805 Drawing no.\n") or ""

            rows.append(
                ft.DataRow(
                    cells=[
                        ft.DataCell(ft.Text(str(item.get("No.", "")))),
                        ft.DataCell(ft.Text(str(item.get("Item", "")))),
                        ft.DataCell(ft.Text(str(item.get("Code", "")))),
                        # စာသားရှည်များ စခရင်ညှပ်မသွားစေရန် max_lines သတ်မှတ်ခြင်း
                        ft.DataCell(ft.Text(str(drawing_val), max_lines=2)),
                        ft.DataCell(ft.Text(str(price_val))),
                    ]
                )
            )

        # ဇယားဆောက်ခြင်း (width ကို page.width မသုံးဘဲ Auto ထားသည်)
        datatable = ft.DataTable(
            columns=columns,
            rows=rows,
            border=ft.border.all(1, ft.colors.GREY_400),
            border_radius=10,
            vertical_lines=ft.border.BorderSide(1, ft.colors.GREY_300),
            horizontal_lines=ft.border.BorderSide(1, ft.colors.GREY_300),
            heading_row_color=ft.colors.BLUE_100,
            heading_row_height=40,
            data_row_max_height=60,
        )

        # ဖုန်းစခရင်ပေါ်တွင် ဘေးတိုက်ရွှေ့ကြည့်နိုင်ရန် Row ထဲသို့ထည့်ပြီး Scroll ပေးခြင်း
        content = ft.Row(
            controls=[datatable],
            scroll=ft.ScrollMode.ALWAYS,  # ဘေးတိုက် အမြဲရွှေ့ကြည့်နိုင်မည်
        )

    # Page ထဲထည့်မယ်
    page.add(
        header,
        ft.Divider(height=10, thickness=2),
        ft.Container(
            content=content,
            padding=10,
            bgcolor=ft.colors.WHITE,
            border_radius=10,
            shadow=ft.BoxShadow(blur_radius=10, color=ft.colors.GREY_300),
        ),
    )

ft.app(target=main)
