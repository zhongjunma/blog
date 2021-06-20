# HTML

## 什么是 HTML？

HTML（**H**yper**T**ext **M**arkup **L**anguage），不是编程语言，是一种标记语言。

以下内容整理自 [学习 HTML ：指南与教程](https://developer.mozilla.org/zh-CN/docs/Learn/HTML)。

- [HTML 基础](html-base-label)

## 标签

### 图像

```html
<img src="images/firefox-icon.png" alt="测试图片">
```

`src` 是图像文件的地址，`alt` 是图像的描述内容（用户视觉障碍、图片加载出错时显示）

### 标题（Heading）

HTML 包含 6 级标题，通常使用 3～4 级就够了。

```html
<h1>主标题</h1>
<h2>顶层标题</h2>
<h3>子标题</h3>
<h4>次子标题</h4>
```

### 段落（Paragraph）

通常用于指定常规的文本内容。

```html
<p>这是一个段落</p>
```

### 列表（List）

1. 有序列表（Ordering list），`<ol></ol>`。
2. 无需列表（Unordering list），`<ul></ul>`。

列表中的每一个项目用 `<li></li>` 来包围。

```html
<p>Mozilla 是一个全球社区，这里聚集着来自五湖四海的</p>

<ul>
  <li>技术人员</li>
  <li>思考者</li>
  <li>建造者</li>
</ul>

<p>我们致力于……</p>
```

### 链接（Anchor）

```html
<a href="https://www.mozilla.org/zh-CN/about/manifesto/">Mozilla 宣言</a>
```

元素的属性 `href` 指的是“超文本引用（**h**ypertext **ref**erence）”，`href` 的指就是网址的链接，元素的内容是网址的描述内容。
