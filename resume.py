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
    st.image("https://cdn-icons-png.flaticon.com/512/3135/3135715.png", width=150)

with col2:
    st.title("润松阁")
    st.subheader("人生意向：活到老学到老，学无止境其乐无穷！")
    st.write("📞 电话：131-xxxx-5571")
    st.write("📧 邮箱：3045142985@qq.com")
    st.write("📍 现居地：广州 · 增城新塘")
    st.write("🔗 GitHub：github.com/rongsongge")
    st.write("🔗 个人博客：50218782704001dd.com")

st.divider()

# ---------------------- 个人简介 ----------------------
st.header("👤 个人简介")
st.write("""
- 拥有 X 年数据分析 / Python 开发经验，熟练使用 Pandas、Matplotlib、Streamlit 等工具进行数据处理与可视化。
- 擅长自动化报表开发、数据看板搭建，可独立完成从需求分析到落地交付的全流程。
- 熟悉 Excel 高级函数、MySQL 数据库基础操作，具备良好的业务理解能力与沟通能力。
- 做事严谨、学习能力强，乐于接受新挑战，希望在数据相关岗位持续成长。
""")

st.divider()

# ---------------------- 技能清单 ----------------------
st.header("💡 技能清单")
col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("**技术工具**")
    st.progress(90, text="Python / Pandas")
    st.progress(85, text="Streamlit")
    st.progress(80, text="SQL / MySQL")

with col2:
    st.markdown("**数据能力**")
    st.progress(85, text="数据清洗与分析")
    st.progress(80, text="数据可视化")
    st.progress(75, text="自动化报表")

with col3:
    st.markdown("**办公工具**")
    st.progress(95, text="Excel / WPS")
    st.progress(80, text="PPT / 汇报")
    st.progress(70, text="Git / 版本控制")

st.divider()

# ---------------------- 工作经历 ----------------------
st.header("💼 工作经历")

st.subheader("新塘成校| 塘泽教育")
st.write("📅 2000.03 - 至今 | 广州")
st.markdown("""
- 负责业务数据的日常监控与分析，搭建自动化日报/月报体系，每月节省 40+ 小时人工操作。
- 使用 Streamlit 开发内部数据看板，实现销售数据、用户行为数据的实时可视化展示，提升团队决策效率。
- 对接业务部门需求，输出数据报告与分析结论，支撑业务优化与运营策略调整。
- 负责数据清洗与治理工作，规范数据口径，提升数据准确性与可用性。
""")

st.divider()

# ---------------------- 教育经历 ----------------------
st.header("🎓 教育经历")
st.subheader("XX大学 | 计算机科学与技术 | 本科")
st.write("📅 2018.09 - 2022.06")
st.write("主修课程：Python 编程、数据库原理、数据结构、统计学、数据挖掘")

st.divider()

# ---------------------- 项目经历 ----------------------
st.header("🚀 项目经历")

st.subheader("1. 自动化数据分析报表系统")
st.write("**技术栈：Python + Pandas + Streamlit**")
st.markdown("""
- 开发了一套可在线使用的数据分析工具，支持上传 Excel/CSV 文件，自动完成数据清洗、分析与可视化。
- 内置常用图表模板，一键生成业务分析报告，可直接导出为图片或 PDF。
- 已在团队内部推广使用，显著提升了同事们的数据分析效率。
""")

st.subheader("2. 个人简历网站（本项目）")
st.write("**技术栈：Python + Streamlit**")
st.markdown("""
- 纯 Python 开发的在线简历网站，无需前端代码即可快速搭建和更新。
- 支持自定义主题样式，可轻松修改为个人专属风格。
""")

st.divider()

# ---------------------- 页脚 ----------------------
st.markdown(
    """
    <div style="text-align: center; color: #888;">
    ✨ 感谢您查看我的简历，期待与您进一步沟通！
    </div>
    """, unsafe_allow_html=True
)
