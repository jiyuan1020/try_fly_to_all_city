import requests
import os
import re

# 你的代理服务器信息
# 格式为 'SOCKS5 IP:端口;' 或 'PROXY IP:端口;'
MY_PROXY_RULE = 'SOCKS5 fly.appendata.cn:1999;'
# 如果你希望在代理失效时直接连接，可以在后面加上 'DIRECT;'
# MY_PROXY = "SOCKS5 fly.appendata.cn:1999; DIRECT;"

# 原始 PAC 文件链接
PAC_URL = "https://raw.githubusercontent.com/petronny/gfwlist2pac/master/gfwlist.pac"

def update_pac_file():
    print("正在下载最新的 PAC 文件...")
    try:
        # 获取原始 PAC 文件内容
        response = requests.get(PAC_URL)
        response.raise_for_status()
        original_pac_content = response.text
        
        # 使用正则表达式替换代理服务器信息
        # 匹配 var proxy = '...'，并替换引号内的内容
        # 如果原始文件中有多个 proxy 变量，这个正则可能需要微调
        modified_pac_content = re.sub(
            r"var proxy = '[^']';", 
            f"var proxy = '{MY_PROXY_RULE} DIRECT';", # 默认加上 DIRECT 以防代理失效
            original_pac_content
        )
        
        # 保存修改后的 PAC 文件
        with open("proxy.pac", "w", encoding='utf-8') as f:
            f.write(modified_pac_content)
        
        print("PAC 文件更新成功，并已替换代理服务器信息。")

    except Exception as e:
        print(f"更新 PAC 文件时发生错误：{e}")
        return False
    return True

if __name__ == "__main__":
    update_pac_file()