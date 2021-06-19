# CSS 基础

## 什么是 CSS？

CSS（Cascading Style Sheet，层叠样式表）是为网页添加样式的代码。跟 HTML 一样，CSS 也不是编程语言。CSS 也不是标记语言，是样式表语言。

想要修改 HTML 中的样式，需要在 HTML 的标签 `head` 中添加链接的代码：

```html
<link href="styles/style.css" rel="stylesheet">
```

## 规则集

CSS 的结构称为规则集。

```css
p {
    color: red;
}
```

![规则集](../images/web/css-declaration.png)

规则集的结构：

- 选择器（selector），HTML 元素的名称
- 声明（declaration），`color: red;` 在这里就是一个声明，是一个单独的规则。添加指定样式元素的属性。
- 属性（properties），`color`，改变 HTML 元素样式。
- 属性的值（property value），`red`，属性的冒号后边，分号前边。

CSS 的其他语法：

- 规则集在大括号内 `{}`。
- 属性和属性值之间有冒号 `:`。
- 声明要用分号 `;` 隔开。
- 选择器中包含多个元素使用逗号 `,` 隔开。
- `/*注释内容*/`

选择器有多种类型，具体参阅[CSS 选择器](https://developer.mozilla.org/en-US/docs/Learn/CSS/Building_blocks/Selectors)

## 一切皆盒子

CSS 布局主要基于盒模型：

![盒模型](../images/web/box-model.png)

- `padding`，内边距
- `border`，边框
- `margin`，外边距
