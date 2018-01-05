from data_export import html_data_process, write_json_to_file

html_json = html_data_process()

write_json_to_file("jdk_html.json", html_json)
