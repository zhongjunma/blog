(html-element)=
# HTML 元素

## 元素基础

HTML 由一系列元素（elements）组成。一个元素的例子：

```html
<p class="editor-note">我的猫咪脾气爆</p>
```

元素包括：

1. 开始标签（Opening tag）`<p>`。
2. 结束标签（Closing tag）`</p>`。
3. 内容（Content）`我的猫咪脾气爆`。
4. 属性（Attribute）`class="editor-note"`，其中，`class` 是属性名称，`editor-note` 是属性值。

一些重要的概念：

- 块级元素
- 嵌套元素
- 内联元素
- 空元素

### 嵌套元素

将元素放在元素中，称为嵌套元素。

```html
<p class="editor-note">我的猫咪脾气<strong>爆</strong></p>
```

显示如下：

<p class="editor-note">我的猫咪脾气<strong>爆</strong></p>

### 块级元素和内联元素

块级元素在页面中以块的形式出现，也就是说块级元素元素会另起一行。块级元素可以嵌套在其他块级元素中，但是不可以嵌套进内联元素中。比如：

- 段落元素 `<p>`
- 列表元素 `<ol>`、`<ul>`

内联元素通常出现在块级元素中，比如

- 超链接元素 `<a>`
- 强调元素 `<em>`、`<strong>`

```html
<!-- 内联元素 -->
<em>第一</em><em>第二</em><em>第三</em>
<!-- 块级元素 -->
<p>第四</p><p>第五</p><p>第六</p>
```

显示如下：

<em>第一</em><em>第二</em><em>第三</em>
<p>第四</p><p>第五</p><p>第六</p>

### 空元素

空元素没有内容，也没有开始标签、结束标签，只有一个标签。例如：

```html
<img src="image.png" alt="图片">
```

## 属性基础

属性包含了元素的额外信息，通常不会出现在实际的内容中。一个属性必须包括：

1. 一个空格，用于分隔元素名称和属性。
2. 属性名称，后面有等于号 `=`。
3. 属性值，由引号 `""` 引起来。

```html
<!-- 这个空元素包含了两个属性 -->
<img src="image.png" alt="图片">
```

### 布尔属性

布尔属性没有属性值，它的属性值和属性名称相同，例如：

```html
<input type='text' disabled>
<input type='text'>
```

显示如下：

<input type='text' disabled>
<input type='text'>

这里的 `disable` 属性表示表单输入不可用。

## HTML 头部元素

HTML 中的 `<head>` 元素中的内容不会显示在浏览器中，它的作用是保存一些元数据。

```{note}
Metadata 元数据，描述数据的数据。比如，一个 HTML 文件是一份数据，HTML 的 `<head>` 元素中也包含了描述 HTML 的元数据（文档作者和概要）。
```

与头部元素相关的元素包括：

- 标题
- `<meta>` 元素
- 自定义图标
- 引入 CSS
- 设定文档的主语言

大型页面的 `<head>` 中会包含很多元数据，以下是一个简短的例子：

```html
<head>
    <meta charset="UTF-8">
    <title>测试页面</title>
</head>
```

```html
<head>
    <!-- 指定文档的字符编码 -->
    <meta charset="UTF-8">

    <!-- 添加 HTML 的作者和描述 -->
    <meta name="author" content="Ma Zhongjun">
    <meta name="description" content="这是一个测试页面">

    <!-- 整个 HTML 文档的标题，注意区别<h1>，<h1>是内容的标题 -->
    <title>测试页面</title>

    <!-- 自定义图标 -->
    <link rel="shortcut icon" href="favicon.ico" type="image/x-icon">

    <!-- 应用 CSS -->
    <link rel="stylesheet" href="my-css-file.css">
</head>
```

```{note}
`<h1>` 也是标题，但是是页面内容的标题，在 `<body>` 中，要注意区分两者。
```
