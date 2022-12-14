# 分刀查轴

分刀查轴是一个适用于公主连结公会战的辅助插件，帮助您更好的分刀

（现在还有sb写pcr插件，不会吧不会吧）

### ★ 如果你喜欢的话，请给仓库点一个star支持一下23333 ★

## 本项目地址：

https://github.com/SonderXiaoming/fendao

## 安装方法：

- 将`fendao`文件夹复制到`hoshino\modules`文件夹下；
- 最后记得在`hoshino\config\__bot__.py`的`MODULES_ON`中加上`fendao`

### 查轴指令帮助：

查轴 [阶段] [类型] [BOSS] [作业序号]

阶段：ABCD，对应公会战的四个阶段，留空表示A面

类型：T 代表自动刀，W 代表尾刀，S代表手动刀，填写多个代表都行，留空表示我全要

BOSS：1-5，对应公会战的一至五王，填写多个代表都行，留空表示我全要

作业序号：花舞作业的序号，如‘A101’，可以省略

### 指令示例：

| 指令        | 说明                                     |
| ----------- | ---------------------------------------- |
| 查轴 A      | (查询一阶段的所有作业信息)               |
| 查轴 A101   | (详细查询特定作业)                       |
| 查轴 A S    | (查询一阶段的手动作业信息)               |
| 查轴 A 1    | (查询一阶段一王的所有作业信息)           |
| 查轴 A T 1  | (查询一阶段一王的AUTO刀作业信息)         |
| 查轴 A TS 1 | (查询一阶段一王的AUTO刀和手动刀作业信息) |

注：指令示例中的空格均不可省略。

### 分刀指令帮助：

分刀 [阶段] [毛分/毛伤] (类型) (BOSS) 

阶段：ABCD，对应公会战的四个阶段，支持跨面，如‘CCD’，和后面boss一一对应，只填写一个默认全是这一阶段

类型：T 代表自动刀，W 代表尾刀，S代表手动刀，填写多个代表都行，留空表示我全要

BOSS：1-5，对应公会战的一至五王，可以‘123’或者‘12’,也可以‘555’,留空表示哪个boss无所谓

作业序号：列表中作业的序号

### 指令示例：

| 指令              | 说明                                                |
| ----------------- | --------------------------------------------------- |
| 分刀 A 毛分       | (查询一阶段的所有分刀可能，按分数排序)              |
| 分刀 A 毛分 T     | (查询一阶段一王的AUTO刀所有分刀可能，按分数排序)    |
| 分刀 A 毛分 T 123 | (查询一阶段的1,2,3王所有AUTO刀分刀可能，按分数排序) |

注：指令示例中的空格均不可省略。

### 自定义box

| 指令                          | 说明                                   |
| ----------------------------- | -------------------------------------- |
| 【添加角色黑名单】 + 角色名称 | （支持多角色，例如春环环奈，无空格）   |
| 【添加角色缺失】 + 角色名称   | （支持多角色，例如春环环奈，无空格）   |
| 【添加作业黑名单】 + 作业id   | （作业序号：花舞作业的序号，如‘A101’） |
| 【删除角色黑名单】 + 角色名称 | （支持多角色，例如春环环奈，无空格）   |
| 【删除角色缺失】 + 角色名称   | （支持多角色，例如春环环奈，无空格）   |
| 【删除作业黑名单】 + 作业id   | （作业序号：花舞作业的序号，如‘A101’） |
| 【查看角色缺失】              | （查看哪些角色缺失）                   |
| 【查看角色黑名单】            | （查看哪些角色是黑名单）               |
| 【查看作业黑名单】            | （查看哪些作业是黑名单）               |
| 【清空角色缺失】              | （清空角色缺失）                       |
| 【清空角色黑名单】            | （清空角色黑名单）                     |
| 【清空作业黑名单】            | （清空作业黑名单）                     |

=============================================

数据来源于: https://www.caimogu.cc/gzlj.html

## 备注

Q：能不能自动上号根据剩余box和刀自动配对

A：可以，已经写了，但涉及登录账号，阉割了（如果你哪里报错或者看见什么神秘代码，那估计就是我删多/少了）

## 特别感谢

[怡宝](https://github.com/watermellye)对分刀逻辑的优化（重写）
