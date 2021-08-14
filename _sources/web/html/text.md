(html-text)=
# 文字处理

## 基础文字处理

- 标题
- 段落
- 列表
- 重点强调

```{note}
注意语义元素与表象元素的区别，两者虽然都改变了文字的外观，但表象元素并不代表特殊含义。
```

### 标题
HTML 包含 6 级标题，在同一个页面中通常使用 3～4 级就够了。

```html
<h1>主标题</h1>
<h2>顶层标题</h2>
<h3>子标题</h3>
<h4>次子标题</h4>
```

```{note}
- 切记不要使用过多级标题，这样会导致混乱。
- 一级标题 `<h1>` 在一个页面中只使用一次。
- 层次结构要合理。
```

### 段落

段落通常用于指定常规的文本内容。

```html
<p>这是一个段落</p>
```

```{note}
`<h1>` 是一个语义元素。我们看到什么，就知道他要代表什么，`<h1>` 告诉我们标题是什么，而不是简单改变这段文字的样式。
```

### 列表

1. 有序列表（Ordering list），`<ol></ol>`。
2. 无需列表（Unordering list），`<ul></ul>`。

列表中的每一个项目用 `<li></li>` 来包围。

```html
<ul>
  <li>技术人员</li>
  <li>思考者</li>
  <li>建造者</li>
</ul>

<ol>
  <li>技术人员</li>
  <li>思考者</li>
  <li>建造者</li>
</ol>
```

显示如下：

<ul>
  <li>技术人员</li>
  <li>思考者</li>
  <li>建造者</li>
</ul>

<ol>
  <li>技术人员</li>
  <li>思考者</li>
  <li>建造者</li>
</ol>

列表也是可以嵌套的，例如：

```html
<ul>
  <li>技术人员</li>
  <li>思考者</li>
  <li>建造者</li>
  <ol>
    <li>技术人员</li>
    <li>思考者</li>
    <li>建造者</li>
    </ol>
</ul>
```

显示如下：

<ul>
  <li>技术人员</li>
  <li>思考者</li>
  <li>建造者</li>
  <ol>
    <li>技术人员</li>
    <li>思考者</li>
    <li>建造者</li>
    </ol>
</ul>

### 重点强调

强调 `<em>`，即 emphasis。

```html
<p>用<em>斜体</em>表示强调的字。</p>
```

显示如下：

<p>用<em>斜体</em>表示强调的字。</p>

非常重要 `<strong>`。

```html
<p>用<strong>粗体</strong>字强调重要的字。</p>
```

显示如下：

<p>用<strong>粗体</strong>字强调重要的字。</p>

```{note}
`<em>` 和 `<strong>` 都是语义元素。屏幕阅读器能够识别出来，而不是单纯的斜体和加粗。斜体 `<i>`、加粗 `<b>` 都是表象元素，只改变外观，不表示强调。
```

## 高级文字排版

- 超链接
- 描述列表
- 代码
- 引用
- 缩略语
- 联系方式
- 上标下标
- 时间日期

### 超链接

超链接（hyperlink），是允许我们同其他网页或站点之间进行链接的元素。`<a>` 元素可以将文本转化为链接。

```html
<p>这是一个指向
    <a href="https://www.mozilla.org/zh-CN/about/manifesto/" title="了解 Mozilla 的使命">
        Mozilla 宣言
    </a>
    的超链接
</p>
```

显示如下：

<p>这是一个指向
    <a href="https://space.bilibili.com/672353429" title="关注贝拉">
        贝拉
    </a>
    的超链接
</p>

`<a>` 元素指的是 **a**nchor（锚点），属性 `href` 指的是 **h**ypertext **ref**erence（超文本引用），`href` 的值就是网址的链接，属性 `title` 是链接的标题，当鼠标悬停到超链接上时，就会显示 `title` 的值，元素的内容是变为超链接的文本。

```{note}
注意区分元素属性 `title` 以及元素的内容，`title` 是鼠标悬停时的文字，元素的内容始终显示在页面上。
```

同样地，也可以将块级元素转化为块级链接。例如，我们将图像转化为链接。

```html
<a href="https://space.bilibili.com/672353429" title="贝拉">
    <img src="bella.gif" alt="贝拉">
</a>
```

显示如下：

<a href="https://space.bilibili.com/672353429" title="贝拉">
    <img src="../../_images/bella.gif" alt="贝拉">
</a>

### 描述列表

`<dl>`（**d**escription **l**ist），用于标记一组项目及其相关描述，例如术语和定义。`<dl>` 中的每一项使用 `<dt>`（description term），每一个描述使用 `<dd>`（description description）闭合。例如：

```html
<dl>
  <dt>碇真嗣</dt>
    <dd>初号机驾驶员</dd>
  <dt>明日香</dt>
    <dd>二号机驾驶员</dd>
    <dd>不傲不娇不是金发不是双马尾</dd>
  <dt>绫波丽</dt>
    <dd>零号机驾驶员 </dd>
</dl>
```

显示如下：

<dl>
  <dt>碇真嗣</dt>
    <dd>初号机驾驶员</dd>
  <dt>明日香</dt>
    <dd>二号机驾驶员</dd>
    <dd>不傲不娇不是金发不是双马尾</dd>
  <dt>绫波丽</dt>
    <dd>零号机驾驶员 </dd>
</dl>

```{note}
一项 `<dt>` 中可能包含有多条描述 `<dd>`。
```

### 引用

使用 `<blockquote>` 块级内容转化为块引用，样式改变。一般会有缩紧。

```html
<blockquote cite="https://zhongjunma.github.io/blog/intro.html">
    小马的博客
</blockquote>
```

显示如下：

<blockquote cite="https://zhongjunma.github.io/blog/intro.html">
    小马的博客
</blockquote>

行内引用 `<q>` 同块引用工作方式相同，只不过不换行，并且将内容使用引号 `""` 引起来。

```html
<p>小马的<q cite="https://zhongjunma.github.io/blog/intro.html">博客</q></p>
```

显示如下：

<p>小马的<q cite="https://zhongjunma.github.io/blog/intro.html">博客</q></p>

```{note}
`cite` 属性不会显示在网页中。
```

想要让 `<cite>` 元素显示在网页中，需要添加一个超链接 `<a>`。

```html
<p>小马的<a href="https://zhongjunma.github.io/blog/intro.html"><cite>博客</cite></a></p>
```

显示如下：

<p>小马的<a href="https://zhongjunma.github.io/blog/intro.html"><cite>博客</cite></a></p>

### 缩略语

使用 `<abbr>` 元素包裹缩略语或者缩写，并在 `title` 元素中提供解释，鼠标悬停皆可查看解释。

```html
<p>我在学习 <abbr title="Hyper text Markup Language">HTML</abbr> 的基础知识。</p>
```

显示如下：

<p>我在学习 <abbr title="Hyper text Markup Language">HTML</abbr> 的基础知识。</p>

### 联系方式

仅用于标记联系方式。

```html
<address>
    <p>小马，北京，中国</p>
</address>
```

显示如下：

<address>
    <p>小马，北京，中国</p>
</address>

### 上标和下标

```html
<p>x<sub>i</sub>，y<sup>j</sup></p>
```

显示如下：

<p>x<sub>i</sub>，y<sup>j</sup></p>

### 代码

- `<code>` 用来标记代码。
- `<pre>` 用来保留空白符，可以结合 `<code>` 来标记代码块。

```
<code>import pandas as pd</code>

<pre><code>
def add(x, y):
    return x+y
</code></pre>
```

显示如下：

<code>import panda as pd</code>

<pre>
<code>def add(x, y):
    return x+y</code>
</pre>

### 时间日期

`<time>` 元素提供了可供机器识别的时间日期格式，并不会展示在界面上。当然，`datetime` 的有很多种可被机器识别的格式。

```html
<time datetime="2021-06-22">2021年6月22日</time> 
```

显示如下：

<time datetime="2021-06-22">2021年6月22日</time> 
