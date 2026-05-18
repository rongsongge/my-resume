import streamlit as st

# ---------------------- 页面基础配置 ----------------------
st.set_page_config(
    page_title="个人简历 | 润松阁",
    page_icon="📄",
    layout="wide",  # 宽屏更适合简历排版
    initial_sidebar_state="collapsed"
)

# ---------------------- 自定义主题样式 ----------------------
# 你可以修改这里的颜色来改变简历整体风格
st.markdown("""
<style>
    .main {
        background-color: #F5F7FA;
    }
    .st-emotion-cache-1v0mbdj {
        background-color: white;
        padding: 20px;
        border-radius: 10px;
        box-shadow: 0 2px 5px rgba(0,0,0,0.1);
    }
    h1, h2, h3 {
        color: #2E4053;
    }
    .st-emotion-cache-16idsys p {
        color: #333333;
    }
</style>
""", unsafe_allow_html=True)

# ---------------------- 个人信息头部 ----------------------
# 两列布局：左边头像，右边个人信息
col1, col2 = st.columns([1, 3])

with col1:
    # 头像：可以放本地图片路径，或者直接用网络图片
    # 把下面路径换成你的头像图片路径，比如 "avatar.jpg"
    st.image("rongsongge.png", width=150)

with col2:
    st.title("润松阁")
    st.subheader("人生意向：活到老学到老，学无止境其乐无穷！")
    st.write("📞 电话：131-xxxx-5571")
    st.write("📧 邮箱：13045142985@qq.com")
    st.write("📍 现居地：广州 · 增城新塘")
    st.write("🔗 GitHub：github.com/rongsongge")
    st.write("🔗 Https:share.streamlit.io/")
    st.write("🔗 个人博客：50218782704x01xd.com")

st.divider()

# ---------------------- 个人简介 ----------------------
st.header("👤 不忘历史")
st.write("""
- 生于1966年冬月，出生地那时叫雷港公社合兴大队小埂生产队，后来在淮南读书90年分配到广东坪石，再后来95年底就来到了增城新塘至今。
- 父亲（1940年7月至2015年9月1日）小时候9岁随奶奶流浪逃荒来到此地，老家在哪也不知了，父亲一生辛苦操劳但后中风瘫痪十多年卧床不起。
- 母亲（1947年8月至2025年12月13日）2岁时过寄到小爷爷家我们称外公，6岁生场大病吃错了药智慧一直停留在6至8岁状态，母亲一生善良简朴。
- 有两个弟弟一个妹妹，大弟务农一直在老家，妹外打工嫁在外县离老家较近，小弟打工一直在我身边，同我一起尽心尽力照顾了亲爱母亲十年。
- 92年结的緍，老婆她人很本份善良较顾家，有一女儿，她也很老实独立不让人操心。家庭稳定，生活简朴，与世无争。
- 岳父（1935年11月至2022年2月20日）当过兵性格平静待人生活简朴，每日喝点酒午睡时间长，喜好待在家里看书看看电视，不操心闲事。
- 岳母（1941年12月）以前是小学高级教师，退休前一人在湖南教书，性格好强多操心现在仍不闲着呢。
- 人生中的贵人，小学时有个鲍老师无意中把我名字中的金字改成了劲字，可能真的会影响此生呀。
- 大学毕业时淮南供电所工作的一位同乡请我在外面吃餐饭并借给我60元钱，才有路费从安徽坐火车来到广东坪石，但我后来却不记得他的名字了。
- 95年底以前坪石水泥厂的贺厂长帮我调到广州增城地铁水泥厂工作，使我人生轨迹有了新的转变，从粤北山区来到了广州大城市。
- 2000年底新塘成人学校的朱主任帮我招进了成人文化技术学校当一名电工老师，从此我的人生又转变成了一名聘请教师工作者。
- 2014年底直接进了以前同事的陈老师创办塘泽教育公司上班当一名培训老师一直至今。
""")

st.divider()

# ---------------------- 能作点什么 ----------------------
st.header("💡 一点基础技能清单")
col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("**绘图技术工具**")
    st.progress(90, text="CAD/ 3D")
    st.progress(85, text="CDR/AI/PS")
    st.progress(80, text="SW/PROE/PLAN")

with col2:
    st.markdown("**机电技术**")
    st.progress(85, text="机械设备管理")
    st.progress(80, text="电工技术知识")
    st.progress(75, text="自动化PLC技术")

with col3:
    st.markdown("**办公工具**")
    st.progress(95, text="WORD/EXCEL / ppt")
    st.progress(80, text="AI/ 飞书")
    st.progress(70, text="HTML/ 网页基础")

st.divider()

# ---------------------- 工作经历 ----------------------
st.header("💼 曾经工作经历")

st.subheader("新塘成校| 塘泽教育")
st.write("📅 2000.03 - 至今 | 广州")
st.markdown("""
- 开始时期教过成人大专课程，也教过成人基础英语。
- 教过十多年电工班考证班。
- 教过十年技校模具班课程，七年技校电梯班课程。
- 教的最长时间的是电脑培训方面的课程，差不多有二十多年。
""")

st.divider()

# ---------------------- 教育经历 ----------------------
st.header("🎓 教育经历")
st.subheader("安徽理工大学 | 原矿业学院 | 本科")
st.write("📅 1986.09 - 1990.06")
st.write("主修课程：机电一体化、机械原理、材料力学、机电工程等")

st.divider()

# ---------------------- 项目经历 ----------------------
st.header("🚀 项目经历")

st.subheader("主要工作情况")
st.write("**机电技术**")
st.markdown("""
- 90年参加工作至95年，粤北坪石矿务局，机械厂、水泥厂、供电所。
- 96年至99年地方铁路有限公司、仙村水泥厂。
- 此后从事教育培训方面工作。
""")

st.subheader("2. 个人简历网站（本项目）")
st.write("**开始学习制作网页**")
st.markdown("""
- 纯 Python 制作在线简历网站，无需前端代码即可快速搭建和更新。
- 支持自定义主题样式，可轻松修改为个人专属风格。
""")

st.divider()

# ---------------------- 页脚 ----------------------
st.markdown(
    """
    <div style="text-align: center; color: #888;">
    ✨ 感谢您查看我的简介，让网络世界也有一个无名的我......！
    </div>
    """, unsafe_allow_html=True
)
st.markdown("[👉 点击进入我的个人教学主页](https://tangzediannao.streamlit.app)")
st.markdown("[👉 点击进入我的个人作品一主页](https://rongsongge.github.io/fruitshop/)")
