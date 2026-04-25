import hashlib, os, sys
sys.stdout.reconfigure(encoding='utf-8')
base = r'd:\AI\LLM-WIKI\jiaruo\raw\pdfs'
new_files = [
    'GPAN 机器人应用介绍.pdf',
    '深圳We Accelerate Robotics--传感赋能：半导体创新助力机器人智能进化--梁国信.pdf',
    '深圳We Accelerate Robotics--基于英飞凌PSOC C3与GaN的电机驱动方案--韩兴涛.pdf',
    '深圳We Accelerate Robotics--英飞凌整体解决方案助力机器人高速发展--张强.pdf',
    '深圳We Accelerate Robotics--驱动创新：英飞凌氮化镓解决方案在机器人中的应用--伦伟强.pdf',
    '深圳We Enable AI -- AI 释能：感知、计算、连接--钟至仁.pdf',
    '深圳We Enable AI --人工智能的高速发展需要更广更强的数据安全防护--郑力仁.pdf',
    '深圳We Enable AI --在边缘人工智能中应用英飞凌XENSIV™雷达--周永.pdf',
    '深圳We Enable AI --英飞凌AIROC™无线产品助力AI未来---翁伟钿.pdf',
    '北京主论坛--从WiFi无线感知技术到6G展望：AIoT生态系统中的嵌入式系统开发与技术挑战--佟国香.pdf',
    '深圳We Power AI --人工智能数据中心向更高总线电压的演变及可用解决方案-宋清亮.pdf',
    '深圳We Power AI --英飞凌CoolGaN™赋能AI数据中心--程文涛.pdf',
    '深圳We Power AI --英飞凌为AI服务器提供高效率高功率密度供电方案--卢柱强.pdf',
    '深圳主论坛--2025年度重磅\u201c芯\u201d品全解析--郭晶虹.pdf',
    '深圳主论坛--氮化镓功率器件：技术、应用及未来展望--弓小武.pdf',
]
for f in new_files:
    path = os.path.join(base, f)
    if not os.path.exists(path):
        print(f'NOT FOUND: {f}')
        continue
    h = hashlib.sha256()
    with open(path, 'rb') as fp:
        for chunk in iter(lambda: fp.read(65536), b''): h.update(chunk)
    print(f'{h.hexdigest()}  {f}')
