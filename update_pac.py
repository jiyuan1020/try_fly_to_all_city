import requests
import os
import re

# =========================================================================
# 修改这里：你的代理服务器信息
# =========================================================================
# 格式为 'SOCKS5 你的域名:你的端口;'
MY_PROXY_RULE = 'PROXY china.appendata.cn:31024; SOCKS5 china.appendata.cn:31024; SOCKS china.appendata.cn:31024;'

# 原始 PAC 文件链接
PAC_URL = "https://raw.githubusercontent.com/petronny/gfwlist2pac/master/gfwlist.pac"

def update_pac_file():
    """
    下载原始 PAC 文件，替换代理信息，然后保存。
    """
    print("正在下载最新的 PAC 文件...")
    try:
        # 获取原始 PAC 文件内容
        response = requests.get(PAC_URL)
        response.raise_for_status()  # 如果请求失败，抛出异常
        original_pac_content = response.text
        
        # 使用正则表达式替换代理服务器信息。
        # 这个正则表达式会匹配 'var proxy = ' 后面的任何内容，直到分号。
        modified_pac_content = re.sub(
            r"var proxy = '.*';",
            f"var proxy = '{MY_PROXY_RULE} DIRECT';",
            original_pac_content
        )
        
        # 将修改后的内容保存到 proxy.pac 文件
        with open("proxy.pac", "w", encoding='utf-8') as f:
            f.write(modified_pac_content)
        
        print(f"PAC 文件更新成功。已替换为代理服务器：{MY_PROXY_RULE}")
        
    except requests.exceptions.RequestException as e:
        print(f"网络请求失败，无法下载 PAC 文件：{e}")
        return False
    except Exception as e:
        print(f"更新 PAC 文件时发生错误：{e}")
        return False
    
    return True

if __name__ == "__main__":
    if update_pac_file():
        print("所有步骤已完成。")
