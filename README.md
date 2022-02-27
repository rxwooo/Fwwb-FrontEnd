# 废物外包flask前端+后端

## 预期功能
普通用户登录后，可从前端向后端传递待检测图片。
后端接收到图片后将图片相关信息保存至数据库。
图片传递至检测程序检测，获得检测结果后，返回json至前端。
前端根据检测结果进行框体绘制。
普通用户仅可查看自己检测的结果。
管理员登录后可查看所有用户检测结果。
获取当前用户权限内检测结果进行图表绘制及展示。

## TO DO
- [x] 接收前端发送图片
- [x] 返回处理后的图片
- [x] 接收返回检测信息填入结果表格
- [x] 使用数据库保存数据
- [ ] 用户登录系统
- [ ] 普通用户上传图片进行检测，仅可查看自己检测的结果
- [ ] 管理员查看全局检测结果
- [ ] 获取数据库信息进行图表绘制
- [ ] 根据检测结果数据在前端进行框体绘制

---

### 2.26

程序工程量不大，使用sqlite轻量化处理
建立数据库保存image、user、result、class
实现数据库保存上传图片路径、返回检测结果给前端

---

### 2.18

从learning repository迁移至此

实现图片上传下载及json传输检测结果

实现图片比例自适应(虽然用不上)

---

### before 2.18

学习相关知识及demo实现

