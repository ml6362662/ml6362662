# 发布与维护

## 文件用途

- `README.md`：GitHub Profile 首页内容。
- `docs/index.html`：带视频播放器的作品集。
- `docs/assets/`：四段网页优化视频及真实视频封面。
- `PROJECT_NOTES.md`：技术说明、来源与后续数据检查建议。
- `build_showcase.py`：内容和样式生成源；修改后运行 `python build_showcase.py`。

## 在 GitHub 发布

1. 登录 `ml6362662`，创建公开仓库 `ml6362662`。如果同名仓库已存在，先保留原内容，再合并本次文件。
2. 上传本文件夹中的文件和 `docs` 目录至仓库根目录，保持目录结构；不要把 zip 本身当成网页上传。
3. 在仓库 Settings → Pages 中选择 Deploy from a branch，分支选择 `main`、目录选择 `/docs`，保存。
4. 等待 Pages 部署完成，检查 `https://ml6362662.github.io/ml6362662/`。此 URL 是预设发布地址，未上线前不可访问。
5. GitHub 个人页自动显示同名公开仓库根目录的 README。把 Pages URL 填入个人资料的 Website 字段便于访问。

若使用其他仓库名，请同步替换 README 中的 Pages URL。所有网页内部素材链接为相对路径，无需修改。

官方说明：[Profile README](https://docs.github.com/en/account-and-profile/how-tos/profile-customization/managing-your-profile-readme) · [GitHub Pages](https://docs.github.com/en/pages/quickstart)

## 本地查看

直接用浏览器打开 `docs/index.html` 即可，也可以在此目录运行 `python -m http.server 8765 --directory docs` 并访问 `http://localhost:8765`。

## 视频

复用工作区已有的网页转码素材：H.264、yuv420p、faststart、无音轨。四段合计约 24 MB，保留原始视频不变。六宫格和四宫格保留原构图，竖屏双臂视频使用播放器适配，不裁掉实验内容。

未来更新视频时同步替换 poster，并更新 `docs/assets/media-manifest.json`。若修改成功率，请同步维护 README、网页和 PROJECT_NOTES 的实验阶段口径。
