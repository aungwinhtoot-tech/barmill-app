import flet as ft
from data import ITEMS  # data.py မှ ဒေတာကို ခေါ်သုံးခြင်း

def main(page: ft.Page):
    page.title = "Barmill Offer Viewer"
    page.theme_mode = ft.ThemeMode.DARK
    page.padding = 15

    # ရှာဖွေရန် စာရိုက်ကွက်
    search_input = ft.TextField(
        hint_text="Code၊ Description သို့မဟုတ် Item ဖြင့် ရှာရန်...", 
        expand=True,
        on_change=lambda e: update_list(search_input.value)
    )
    
    results_list = ft.ListView(expand=True, spacing=10)

    def update_list(search_query=""):
        results_list.controls.clear()
        query = search_query.lower()
        
        count = 0
        for item in ITEMS:
            if (query in item['code'].lower() or 
                query in item['desc'].lower() or 
                query in item['item'].lower()):
                
                if count >= 100: 
                    break
                
                results_list.controls.add(
                    ft.Card(
                        content=ft.Container(
                            padding=15,
                            content=ft.Column([
                                ft.Row([
                                    ft.Text(f"Item: {item['item']}", weight=ft.FontWeight.BOLD, color=ft.colors.AMBER_400),
                                    ft.Text(f"Code: {item['code']}", color=ft.colors.BLUE_400, weight=ft.FontWeight.BOLD),
                                ], alignment=ft.MainAxisAlignment.SPACE_BETWEEN),
                                ft.Divider(color=ft.colors.GREY_700),
                                ft.Text(item['desc'], size=14, color=ft.colors.WHITE70),
                                ft.Row([
                                    ft.Text(f"No: {item['no']}", size=12, color=ft.colors.GREY_500),
                                    ft.Text(f"Price: ${item['price']}", weight=ft.FontWeight.BOLD, color=ft.colors.GREEN_400),
                                ], alignment=ft.MainAxisAlignment.SPACE_BETWEEN)
                            ])
                        )
                    )
                )
                count += 1
        page.update()

    page.add(
        ft.Column([
            ft.Row([search_input]),
            ft.Text("ရှာဖွေတွေ့ရှိသည့် ရလဒ်များ (အများဆုံး အခု ၁၀၀ ပြပေးပါသည်)-", size=11, color=ft.colors.GREY_500),
            results_list
        ], expand=True)
    )
    
    update_list()

ft.app(main)

