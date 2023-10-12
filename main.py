import flet as ft

def on_dialog_result(e: ft.FilePickerResultEvent):
    print("Selected files:", e.files)
    print("Selected file or directory:", e.path)



def main(page: ft.Page):
    filePicker = ft.FilePicker(on_result=on_dialog_result)

    def upload_files(e):
        upload_list = []
        if filePicker.result != None and filePicker.result.files != None:
            for f in filePicker.result.files:
                upload_list.append(
                    ft.FilePickerUploadFile(
                        f.name,
                        upload_url=page.get_upload_url(f.name, 600),
                    )
                )
            filePicker.upload(upload_list)

    btn = ft.ElevatedButton("Choose files...",
    on_click=lambda _: filePicker.pick_files(allow_multiple=True))

    btn2 = ft.ElevatedButton("Upload", on_click=upload_files)

    page.overlay.append(filePicker)
    page.add(btn)
    page.add(btn2)
    page.update()

ft.app(target=main)