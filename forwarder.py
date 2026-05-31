from telethon import TelegramClient, events
import asyncio

api_id = 
api_hash = ''

# 采用公用的 api_id 与 api_hash
# 有效避免无法申请和封号风险


SOURCE_CHANNEL = -100
# 替换为源频道 ID
TARGET_CHANNEL = -100
# 替换为目标频道 ID

# 将获取来的 BOTID 填写到 -100 后面即可

client = TelegramClient('my_session', api_id, api_hash, connection_retries=None)

# 处理相册（多图）
@client.on(events.Album(chats=SOURCE_CHANNEL))
async def album_handler(event):
    # 等待 0.5 秒确保所有图片句柄都准备好
    await asyncio.sleep(0.5)
    
    # 相册的文字通常在第一张图
    original_text = event.text or ""
    new_text = original_text
    
    try:
        # event.messages 包含了该组所有消息对象
        await client.send_message(
            TARGET_CHANNEL, 
            new_text, 
            file=event.messages, 
            parse_mode='md',
            link_preview=False
        )
        print("成功合并转发相册")
    except Exception as e:
        print(f"册转发失败: {e}")

# 处理单条消息
@client.on(events.NewMessage(chats=SOURCE_CHANNEL))
async def handler(event):
    # 如果是相册的一部分，跳过，交给 Album 处理器
    if event.grouped_id:
        return
        
    original_text = event.raw_text or ""
    new_text = original_text
    
    try:
        await client.send_message(
            TARGET_CHANNEL, 
            new_text, 
            file=event.message.media, 
            parse_mode='md',
            link_preview=False
        )
        print("同步单条消息")
    except Exception as e:
        print(f"条同步失败: {e}")

print("监听中...")
client.start()
client.run_until_disconnected()