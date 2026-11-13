from pathlib import Path
import json, html

ROOT=Path(__file__).resolve().parent
D=ROOT/'docs'; D.mkdir(exist_ok=True)
projects=[
dict(id='xarm-posttraining', num='01', tag='主要工作 / 算法与数据闭环', title='从单目标到多目标：VLA 真机后训练', subtitle='多柔性物体夹取 · 四宫格实验', lead='让策略面对多个可夹取目标，并适应托盘位置变化。', task='面向商超试吃场景，完成面包片夹取、放入杯中与杯子递送；重点验证多面包片与场景布局变化下的操作表现。', role='负责 STEAM + CFG 后训练的真机数据适配、训练设置与部署验证；参与部署 DAgger 式采集及其 GUI，组织人类接管纠错与多目标数据增采。', method='以综合成功率约 90%、对面包位置适应较好的策略自主 Rollout；在即将失败时人工接管，完成局部纠错后交回策略。将纠错片段与新增多面包示范用于数据迭代，按此前验证的数据要求开展 STEAM + CFG 离线后训练。', result='多面包片夹取综合成功率 >90%；对托盘移动表现出一定适应能力。', limit='杯子位置变化的泛化仍不足；当前结果来自已测试工况，不能外推为任意场景泛化。', tags=['π₀.₅','Human-in-the-loop','DAgger','STEAM + CFG']),
dict(id='xarm-sft', num='02', tag='主要工作 / 真机系统工程', title='Quest 3 × xArm：采集、训练与推理全流程', subtitle='单面包片商超试吃 · 六宫格实验', lead='把 VR 示教、机器人控制与 VLA 真机推理接成可运行的工程链路。', task='夹取托盘中的单个面包片，放入杯子，再夹取杯子递给顾客；视频以六宫格展示不同面包位置下的操作。', role='完成 xArm 真机调试、Quest 3 VR 遥操通信联调与全流程设计；编写遥操 GUI 和真机推理 GUI，参与各环节细节设计，完成采训推集成。', method='接入相机与机器人状态，完成遥操作示教、LeRobot v2.1 数据记录及标注，再进行 π₀.₅ SFT 和真机部署评估。简历记录 xArm 专家示范与 DAgger 式交互数据累计 600+ 条。', result='当前展示阶段，单面包片任务成功率 >90%。', limit='该阶段仅使用 SFT；多面包片、托盘位置和杯子位置变化的泛化不足，因此进一步开展数据闭环与离线后训练。', tags=['Quest 3','xArm','VR Teleoperation','LeRobot','SFT']),
dict(id='agilex-long-horizon', num='03', tag='进阶探索 / 长程操作与方法验证', title='松灵双臂：从物体入杯到杯子堆叠', subtitle='组合操作 · STEAM + CFG 复现', lead='把简单放置扩展为具有阶段依赖的长程任务。', task='先夹取小物体并放入杯中，再夹取杯子并堆叠至另一位置，验证多个操作阶段的连续执行。', role='在前期合作任务基础上参与更复杂的真机实验；同时在服务器复现与验证 STEAM + CFG，梳理训练配置和真机数据要求。', method='使用 RoboTwin adjust_bottle 任务的 50 条专家轨迹验证后训练流程，厘清数据格式、时序样本与训练设置，并总结真机采集文档，为 xArm 实验迁移积累经验。', result='完成长程任务视频展示与后训练方法复现验证，形成真机采集要求的经验总结。', limit='RoboTwin 验证与松灵视频是并行工作；不将此视频表述为 STEAM + CFG 已在松灵真机上取得量化提升的证据。', tags=['AgileX','Long-horizon','RoboTwin','50 expert trajectories']),
dict(id='agilex-foundation', num='04', tag='早期探索 / 工程基础与奖励建模', title='松灵机械臂：从一次杯子放置开始', subtitle='协作完成采训推 · 时序进度价值探索', lead='建立真机数据、SFT 训练与部署推理的工程基础。', task='完成简单杯子放置任务，为后续更复杂、长时序的组合操作建立基础。', role='与团队共同完成数据采集、格式修改适配、SFT 离线训练与真机推理，在实践中掌握采集要求和部署流程。', method='参考 RynnValue 的目标条件时间距离建模思路，围绕阶段时序进度探索奖励设计：预测当前观察距离任务目标的剩余时间，并研究将价值变化用作更密集的学习反馈；完成初步测试验证。', result='积累真实机器人采训推经验，并为复杂任务的奖励建模建立方法基础。', limit='这是基于已有方法的适配探索，不宣称原创 RynnValue，也不以初步测试宣称已解决稀疏奖励信用分配问题。', tags=['Team collaboration','SFT','Temporal distance','Reward / Value'])
]
(ROOT/'projects.json').write_text(json.dumps(projects,ensure_ascii=False,indent=2),encoding='utf8')
def vid(p):
    i=p['id']
    return f'<video controls playsinline preload="none" poster="assets/{i}.jpg" aria-label="{p["subtitle"]}"><source src="assets/{i}.mp4" type="video/mp4">浏览器不支持视频，请使用下方链接打开。</video><figcaption>{p["subtitle"]}<a href="assets/{i}.mp4">打开视频 ↗</a></figcaption>'
cards=''
for p in projects:
    cards+=f'''<article id="{p['id']}" class="project"><div class="project-top"><span class="number">{p['num']}</span><div><p class="eyebrow">{p['tag']}</p><h3>{p['title']}</h3><p class="lead">{p['lead']}</p></div></div><figure>{vid(p)}</figure><div class="tags">{''.join('<span>'+x+'</span>' for x in p['tags'])}</div><div class="details"><div><h4>任务与场景</h4><p>{p['task']}</p><h4>我的贡献</h4><p>{p['role']}</p></div><div><h4>方法与实现</h4><p>{p['method']}</p><h4>实验结果</h4><p>{p['result']}</p></div></div><p class="boundary"><strong>当前边界</strong> {p['limit']}</p></article>'''
page='''<!doctype html><html lang="zh-CN"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1"><meta name="description" content="何非凡的具身智能作品集：Quest 3 与 xArm 真机采训推、DAgger 数据闭环及 STEAM + CFG VLA 后训练。"><meta name="theme-color" content="#f5f3ee"><title>何非凡 | VLA 真机实验与后训练</title><link rel="stylesheet" href="style.css"><link rel="icon" href="assets/favicon.svg" type="image/svg+xml"></head><body><a class="skip" href="#projects">跳到项目</a><header class="wrap"><a class="identity" href="#">HF<span>何非凡 <small>FEIFAN HE</small></span></a><nav aria-label="主导航"><a href="#projects">真机项目</a><a href="#pipeline">技术路线</a><a href="#results">实验结果</a><a href="#about">关于我</a><a href="https://github.com/ml6362662">GitHub ↗</a></nav></header><main><section class="hero wrap"><p class="eyebrow">ROBOT LEARNING / REAL-WORLD EXPERIMENTS</p><h1>让 VLA 在真实世界中<br><em>完成一次可靠的操作。</em></h1><div class="hero-bottom"><p>我是何非凡，北京工业大学控制科学与工程硕士研究生。<br>关注具身智能与 VLA 后训练，把真机调试、数据采集、策略优化与闭环验证连接起来。</p><a class="button" href="#projects">观看真机实验 <span>↓</span></a></div><div class="hero-index"><span>01 / 真机工程</span><span>02 / 人类纠错数据</span><span>03 / 离线后训练</span><span>04 / 泛化评估</span></div></section><section class="feature wrap"><div class="feature-label"><span class="dot"></span> SELECTED DEMO <span>多目标柔性物体夹取</span></div><a href="#xarm-posttraining" aria-label="查看多目标后训练项目"><img src="assets/xarm-posttraining-8.jpg" alt="xArm 在四组真实场景中操作托盘上的多片面包" width="1280" height="720"></a><div class="feature-caption"><strong>从单面包片，到多目标操作。</strong><span>DAgger 数据闭环 × STEAM + CFG</span></div></section><section id="projects" class="wrap"><div class="section-heading"><p class="eyebrow">SELECTED PROJECTS</p><h2>四段实验，一条能力进阶路径。</h2><p>优先展示 xArm 的工程与算法工作，再回看松灵平台上的基础探索。</p></div>'''+cards+'''</section><section id="pipeline" class="pipeline"><div class="wrap"><p class="eyebrow">FROM DEMONSTRATION TO DEPLOYMENT</p><h2>采集不是终点，部署也不是终点。</h2><div class="steps"><div><b>01</b><h3>示教与采集</h3><p>Quest 3 VR 遥操<br>真机、相机与 GUI 联调<br>专家完整轨迹</p></div><div><b>02</b><h3>SFT 基线</h3><p>数据格式适配与标注<br>π₀.₅ 监督微调<br>真机 Rollout 观察</p></div><div><b>03</b><h3>纠错与后训练</h3><p>人工接管、再交回策略<br>多目标示范增采<br>STEAM 优势标签 + CFG</p></div><div><b>04</b><h3>验证与再迭代</h3><p>完整任务执行评估<br>目标数量与位置变化<br>失败归因与数据补充</p></div></div><details><summary>展开：STEAM + CFG 与时间距离奖励的区别</summary><p>STEAM 在 RLinf 中以帧对的时序进度学习 ensemble critic，保守聚合得到逐帧优势标签，再用于 CFG 策略训练。这里的工作重点是复现、真机数据适配与实验验证。人工接管用于采集数据，后续 STEAM + CFG 优化属于离线训练。</p><p>RynnValue 则以任务条件下的剩余时间为价值目标。我的早期探索参考这一思路，将时间距离与阶段进度联系起来研究密集反馈。两条路线分别记录，不把 RynnValue 写成 STEAM 的必要组成部分。</p><p>一种势函数表述为 Φ(s) = −d(s, goal)，奖励塑形项为 γΦ(s′) − Φ(s)。这里用于解释建模思路；实际训练细节与消融结果需以实验配置和日志为准。</p><p><a href="https://rlinf.readthedocs.io/en/latest/rst_source/examples/embodied/steam.html">RLinf STEAM 官方文档 ↗</a> · <a href="https://github.com/alibaba-damo-academy/RynnValue">RynnValue 原始项目 ↗</a></p></details></div></section><section id="results" class="wrap results"><p class="eyebrow">RESULTS & SCOPE</p><h2>结果，连同适用范围一起呈现。</h2><div class="metrics"><div><span>早期完整任务 / 简历记录</span><strong>73% <i>→</i> 94%</strong><p>SFT → STEAM + CFG 后训练</p></div><div><span>当前单面包片 / SFT</span><strong>&gt;90%</strong><p>对应六宫格视频展示阶段</p></div><div><span>当前多面包片 / 后训练</span><strong>&gt;90%</strong><p>多目标夹取综合成功率</p></div></div><p class="note">数字来自本人简历与项目实验总结。早期 73% → 94% 为单列阶段记录，不与当前两组 >90% 混作同一实验对比。各组试验次数、随机种子及布局分布尚未随展示页公开；视频为定性演示，不代表完整评测样本。</p><div class="table-scroll"><table><caption>当前已观察到的能力与边界</caption><thead><tr><th>评估维度</th><th>单面包片 SFT 阶段</th><th>多目标后训练阶段</th></tr></thead><tbody><tr><td>单目标任务</td><td>已验证，成功率 >90%</td><td>持续保留并验证</td></tr><tr><td>多个可夹取目标</td><td>泛化不足</td><td>综合成功率 >90%</td></tr><tr><td>托盘位置变化</td><td>泛化不足</td><td>具备一定适应能力</td></tr><tr><td>杯子位置变化</td><td>泛化不足</td><td>仍待改进</td></tr></tbody></table></div></section><section class="wrap next" id="todo"><p class="eyebrow">NEXT QUESTIONS</p><h2>下一步：让杯子换个位置，任务依然成立。</h2><ol><li><strong>杯子位置泛化</strong><p>系统增采杯子不同位置与相对布局的示范及纠错片段，建立训练布局与未见布局的分离评测。</p></li><li><strong>分阶段失败诊断</strong><p>区分面包夹取、入杯、杯子夹取与递送失败，定位感知、动作或阶段切换问题。</p></li><li><strong>固定协议与消融</strong><p>在相同评测条件下比较 SFT、增加多目标数据、加入纠错数据以及 STEAM + CFG，补充样本数和分项指标。</p></li><li><strong>奖励模型与在线学习</strong><p>继续验证时序进度信号在复杂任务中的作用，探索与真机在线交互训练的结合。</p></li></ol><p class="note">以上为后续计划，不代表已经完成的实验结果。</p></section><section id="about" class="wrap about"><div><p class="eyebrow">ABOUT ME</p><h2>何非凡 <span>Feifan He</span></h2><p>北京工业大学 · 控制科学与工程硕士<br>2023–2027（预计毕业）</p><p>三峡大学 · 自动化本科<br>2019–2023 · 专业排名 5/65</p></div><div><h3>研究与工程关注</h3><p>VLA / Reinforcement Learning / Human-in-the-loop<br>Python · PyTorch · Linux · LeRobot · RLinf</p><p>灵美智能实习期间开展双臂 VLA 训练链路、长时序奖励建模与 xArm 真机后训练。作为学生骨干参与北京市自然科学基金项目“人机共驾强化学习决策优化研究”，独立搭建两代驾驶座舱，开展示范质量评估、反事实接管筛选与质量引导的强化学习，并将相关方法与部署经验延伸至 VLA 后训练。<a href="https://github.com/ml6362662/hil-driving-cockpit">查看座舱科研项目 ↗</a></p><p>中国机器人及人工智能大赛：2025 年国家级一等奖、2026 年国家级三等奖（学生第一，简历记录）。</p><a class="text-link" href="https://github.com/ml6362662">在 GitHub 找到我 ↗</a></div></section></main><footer class="wrap"><span>© 2026 何非凡 · 真实实验，持续迭代。</span><a href="#">返回顶部 ↑</a></footer><script src="main.js"></script></body></html>'''
(D/'index.html').write_text(page,encoding='utf8')
css='''*{box-sizing:border-box}html{scroll-behavior:smooth;scroll-padding-top:30px}body{margin:0;background:#f5f3ee;color:#22332c;font-family:"Segoe UI","Microsoft YaHei",sans-serif;line-height:1.8}a{color:inherit;text-underline-offset:5px}a:hover{color:#a45026}a:focus-visible,summary:focus-visible{outline:3px solid #b65e35;outline-offset:5px}.wrap{max-width:1160px;width:calc(100% - 80px);margin:auto}header{display:flex;align-items:center;justify-content:space-between;min-height:108px;border-bottom:1px solid #d4d7cf}.identity{display:flex;gap:16px;text-decoration:none;font-size:28px;font-weight:750;align-items:center}.identity span{font-size:16px;line-height:1.4}.identity small{display:block;font-size:10px;letter-spacing:2px;font-weight:400}nav{display:flex;gap:27px;font-size:13px}nav a{text-decoration:none}.eyebrow{font-size:11px;letter-spacing:2px;font-weight:650;color:#6a776d;margin:0 0 16px}.hero{padding:64px 0 0}h1{font-size:clamp(32px,4.8vw,58px);line-height:1.35;font-weight:600;letter-spacing:-2px;margin:0}h1 em{font-style:normal;color:#587662}.hero-bottom{display:flex;justify-content:space-between;align-items:center;gap:32px;padding:24px 0 36px}.hero-bottom p{font-size:15px;color:#67716b}.button{background:#294d3b;color:white;text-decoration:none;padding:12px 22px;white-space:nowrap;font-size:14px}.button span{margin-left:30px}.button:hover{background:#40664e;color:#fff}.hero-index{display:flex;justify-content:space-between;border-top:1px solid #d4d7cf;padding:17px 0;font-size:12px;color:#68746b}.feature{margin-top:26px}.feature-label{display:flex;align-items:center;gap:10px;font-size:10px;letter-spacing:2px;margin-bottom:12px}.feature-label span:last-child{margin-left:auto;letter-spacing:0;font-size:12px}.dot{width:6px;height:6px;background:#b66439;border-radius:100%}.feature img{display:block;width:100%;height:auto}.feature-caption{display:flex;justify-content:space-between;padding:15px 0;font-size:13px}.feature-caption span{color:#6c756d}.section-heading{padding:100px 0 35px}h2{font-size:30px;line-height:1.5;font-weight:600;margin:0 0 20px}.section-heading>p:last-child{color:#6e776e;font-size:14px}.project{border-top:1px solid #cfd4cc;padding:40px 0 60px;scroll-margin-top:28px}.project-top{display:flex;gap:28px;margin-bottom:25px}.number{color:#9aa99b;font-size:30px;font-weight:300;line-height:1.3}.project .eyebrow{margin-bottom:8px}h3{margin:0 0 10px;font-size:23px;font-weight:600}.lead{margin:0;color:#737a72;font-size:14px}figure{margin:0;background:#e7e9e2}video{display:block;width:100%;max-height:650px;background:#17211c}figcaption{padding:12px 18px;font-size:12px;color:#5c6a5f;display:flex;justify-content:space-between;gap:15px}.tags{display:flex;flex-wrap:wrap;gap:8px;margin:22px 0}.tags span{font-size:11px;padding:3px 10px;border:1px solid #c9d3c6;border-radius:3px;color:#54705b}.details{display:grid;grid-template-columns:1fr 1fr;gap:50px}h4{font-size:14px;margin:13px 0 8px}.details p{font-size:14px;color:#626c63;margin:0 0 17px}.boundary{font-size:12px;color:#73776a;padding:14px 18px;background:#eceae1;border-left:2px solid #ad9568;margin:12px 0 0}.boundary strong{margin-right:10px}.pipeline{background:#253e30;color:#e5ebe0;padding:65px 0;margin-top:12px}.pipeline .eyebrow{color:#a9bc9f}.steps{display:grid;grid-template-columns:repeat(4,1fr);gap:28px;margin:35px 0}.steps>div{border-top:1px solid #61755d;padding-top:18px}.steps b{font-weight:400;color:#b5c5a4;font-size:13px}.steps h3{font-size:18px;margin-top:16px}.steps p{font-size:13px;color:#bac8b8}.pipeline details{border-top:1px solid #61755d;padding-top:20px;font-size:13px}.pipeline summary{cursor:pointer}.pipeline details p{color:#ced9c8}.results,.next,.about{padding:80px 0}.metrics{display:grid;grid-template-columns:repeat(3,1fr);border-top:1px solid #ccd3c7;border-bottom:1px solid #ccd3c7;padding:30px 0;margin:28px 0 20px;gap:20px}.metrics span{font-size:12px;color:#6e796d}.metrics strong{display:block;font-size:40px;font-weight:500;letter-spacing:-1px}.metrics i{font-size:24px;color:#8a9e84;font-style:normal}.metrics p{font-size:12px;margin:0;color:#6e796d}.note{font-size:12px;color:#7a8073;line-height:1.9}.table-scroll{overflow:auto;margin-top:35px}table{width:100%;border-collapse:collapse;text-align:left;font-size:13px}caption{text-align:left;font-size:15px;font-weight:600;margin-bottom:16px}th,td{padding:15px 18px;border-bottom:1px solid #d8dcd1;white-space:nowrap}th{background:#e9ede3;font-weight:500}.next{border-top:1px solid #d0d6c9;padding-top:60px}.next ol{list-style:decimal-leading-zero;padding-left:36px;display:grid;grid-template-columns:1fr 1fr;gap:30px 60px;margin-top:35px}.next li{padding-left:12px}.next li::marker{color:#8b9b80}.next li p{font-size:14px;color:#6e766b}.about{display:grid;grid-template-columns:1fr 1.2fr;gap:70px;border-top:1px solid #d0d6c9}.about h2 span{font-size:17px;color:#8e9887;font-weight:400}.about p{font-size:14px;color:#677260}.about h3{font-size:18px}.text-link{font-size:14px}footer{display:flex;justify-content:space-between;border-top:1px solid #d0d6c9;padding:25px 0 35px;font-size:11px;color:#808978}.skip{position:absolute;left:-9999px}.skip:focus{left:20px;top:20px;background:white;padding:10px;z-index:3}@media(max-width:700px){.wrap{width:calc(100% - 36px)}header{align-items:flex-start;flex-direction:column;gap:20px;padding:20px 0}nav{gap:18px;font-size:12px;flex-wrap:wrap}.hero{padding-top:40px}h1{letter-spacing:-1px}.hero-bottom{display:block}.hero-bottom p{font-size:13px}.button{display:inline-block;margin-top:14px}.hero-index{flex-wrap:wrap;gap:12px;width:100%;font-size:10px}.feature-caption{display:block}.feature-caption span{display:block;margin-top:4px}.section-heading{padding-top:65px}h2{font-size:25px}h3{font-size:20px}.project-top{gap:16px}.details,.about,.next ol{grid-template-columns:1fr;gap:10px}.steps{grid-template-columns:1fr 1fr}.metrics{grid-template-columns:1fr;gap:25px}.metrics>div+div{border-top:1px solid #d5dbce;padding-top:20px}.metrics strong{font-size:38px}.results,.next,.about{padding:55px 0}.about{gap:25px}figcaption{font-size:10px}.feature-label{letter-spacing:1px}footer{gap:20px}.number{font-size:25px}}@media(prefers-reduced-motion:reduce){html{scroll-behavior:auto}}'''
(D/'style.css').write_text(css,encoding='utf8')
(D/'main.js').write_text("document.querySelectorAll('video').forEach(video=>{video.addEventListener('play',()=>{document.querySelectorAll('video').forEach(other=>{if(other!==video)other.pause()})})});",encoding='utf8')
(D/'.nojekyll').touch()
(D/'assets/favicon.svg').write_text('<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 64 64"><rect width="64" height="64" rx="12" fill="#294d3b"/><text x="32" y="42" text-anchor="middle" font-family="sans-serif" font-size="29" fill="#fff">HF</text></svg>',encoding='utf8')
readme='''# 何非凡 · Feifan He

**北京工业大学 · 控制科学与工程硕士（预计 2027 年毕业）**  
具身智能 / Vision-Language-Action / Reinforcement Learning / Human-in-the-loop

我关注 VLA 从示范学习到真机后训练的落地：完成 Quest 3 VR—xArm 采训推工程，结合人类接管纠错数据与 STEAM + CFG，探索长程操作和多目标泛化。

**[▶ 进入真机视频展示页](https://ml6362662.github.io/ml6362662/)** · [项目技术说明](PROJECT_NOTES.md)

> 四段真实机器人实验。下面按主要成果优先排列；点击封面进入对应项目并播放视频。

'''
for p in projects:
    readme+=f'''## {p['num']} · {p['title']}

[![{p['subtitle']}](docs/assets/{p['id']}.jpg)](https://ml6362662.github.io/ml6362662/#{p['id']})

**任务：** {p['task']}

**我的贡献：** {p['role']}

**实现：** {p['method']}

**结果：** {p['result']}

**局限：** {p['limit']}

[▶ 在线播放](https://ml6362662.github.io/ml6362662/#{p['id']}) · [视频文件](docs/assets/{p['id']}.mp4)

'''
readme+='''## 实验结果与统计范围

| 实验阶段 | 设置 | 结果 |
| --- | --- | --- |
| 早期完整任务（简历记录） | SFT → STEAM + CFG 后训练 | 73% → 94% |
| 当前单面包片阶段 | SFT | 任务成功率 >90% |
| 当前多面包片阶段 | 纠错数据 + 多目标数据 + STEAM / CFG | 综合成功率 >90% |

以上结果属于不同实验阶段，不作跨阶段的直接增益比较。试验次数、布局分布等完整评估记录尚未随主页公开，视频仅作定性演示。

## 后续计划

- [ ] 补充不同杯子位置和相对布局的数据，提升杯子位置泛化。
- [ ] 建立分阶段失败标签，定位夹取、入杯、杯子抓取及递送瓶颈。
- [ ] 固定评估协议，补充试验次数、分项成功率与泛化测试集。
- [ ] 对数据增采、DAgger 纠错与 STEAM + CFG 分别开展消融。
- [ ] 持续探索任务进度奖励与在线强化学习。

## 关于我

- 北京工业大学，控制科学与工程硕士，2023–2027（预计）；三峡大学，自动化本科，2019–2023。
- 灵美智能实习：双臂机器人训练链路与奖励建模、xArm VLA 后训练与真机验证。
- 科研项目：**北京市自然科学基金项目——人机共驾强化学习决策优化研究**（学生骨干）；独立搭建两代驾驶座舱，开展示范质量评估、反事实接管筛选与质量引导的强化学习，积累并延伸至 VLA 后训练的方法与部署能力。[查看座舱科研项目 ↗](https://github.com/ml6362662/hil-driving-cockpit)
- 中国机器人及人工智能大赛：2025 年国家级一等奖、2026 年国家级三等奖（学生第一）。
- 工具与框架：Python、PyTorch、Linux、LeRobot、RLinf。

## 方法来源

感谢 [RynnValue](https://github.com/alibaba-damo-academy/RynnValue) 与 [RLinf STEAM + CFG](https://rlinf.readthedocs.io/en/latest/rst_source/examples/embodied/steam.html) 的开放工作。本文明确区分原始算法贡献与我的工程适配、数据流程、复现和真机实验贡献。

本仓库用于实验展示；未包含团队内部训练代码、模型权重或原始采集数据。
'''
(ROOT/'README.md').write_text(readme,encoding='utf8')
print('Built index.html, CSS, JS, README and project data')
