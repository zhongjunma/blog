(html-head-label)=
# 头部元素

## 什么是 HTML 的头部元素？

HTML 中的 `<head>` 元素中的内容不会显示在浏览器中，它的作用是保存一些元数据。

> Metadata ——元数据，描述数据的数据。比如，一个 HTML 文件是一份数据，HTML 的 `<head>` 元素中也包含了描述 HTML 的元数据（文档作者和概要）。

大型页面的 `<head>` 中会包含很多元数据，以下是一个简短的例子：

```html
<head>
    <meta charset="UTF-8">
    <title>测试页面</title>
</head>
```

## 标题

`<title>` 用于表示整个 HTML 文档的标题，是在 `<head>` 中的元数据。

> `<h1>` 也是标题，但是是页面内容的标题，在 `<body>` 中，要注意区分两者。

## `<meta>` 元素

为 HTML 文档添加元数据需要用到 `<meta>` 元素。

指定文档的字符编码时，如下：

```html
<meta charset="UTF-8">
```

许多 `<meta>` 都包含了两个属性 `name` 和 `content`：

- `name` 指定 `<meta>` 元素的类型
- `content` 指定元数据内容

比如添加 HTML 的作者和描述。在搜索引擎中，描述会被显示在搜索引擎显示的结果中。

```html
<meta name="author" content="Ma Zhongjun">
<meta name="description" content="这是一个测试页面">
```

`<meta>` 也可以向某些网站提供可使用的特定信息。需要遵守这些网站的协议，此处不再赘述，详情可查[此处](https://developer.mozilla.org/zh-CN/docs/Learn/HTML/Introduction_to_HTML/The_head_metadata_in_HTML#%E5%85%B6%E4%BB%96%E7%B1%BB%E5%9E%8B%E7%9A%84%E5%85%83%E6%95%B0%E6%8D%AE)。

## 自定义图标

`<meta>` 中可以设置网站的自定义图标。这个图标通常是 $16\times16$ 像素，这个图标会出现在标签页和收藏夹中。

```html
<link rel="shortcut icon" href="favicon.ico" type="image/x-icon">
```

## 在 HTML 中应用 CSS 和 JavaScript

CSS 如下，`rel="stylesheet"` 表明这是文档的样式表。

```html
<link rel="stylesheet" href="my-css-file.css">
```

JavaScript 通常放在文档的尾部，`</body>` 之前。

```html
<script src="my-js-file.js"></script>
```

> `script` 并不是空元素，因为可以直接把 JS 源码凡在元素内容的位置。

## 设定文档的主语言

这个是在 `<html>` 中设置的：

```html
<html lang="zh-CN">
```

也可以将文档的不同部分设置为不同的语言，例如：

```html
<p>日语实例: <span lang="jp">ご飯が熱い。</span>.</p>
```
