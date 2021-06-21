(html-advanced-text-label)=
# 高级文字排版

## 描述列表

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

## 引用

### 块引用

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

### 行内引用

行内引用 `<q>` 同块引用工作方式相同，只不过不换行，并且将内容使用引号 `""` 引起来。

```html
<p>小马的<q cite="https://zhongjunma.github.io/blog/intro.html">博客</q></p>
```

显示如下：

<p>小马的<q cite="https://zhongjunma.github.io/blog/intro.html">博客</q></p>

```{note}
`cite` 属性不会显示在网页中。
```

### 引文

想要让 `<cite>` 元素显示在网页中，需要添加一个超链接 `<a>`。

```html
<p>小马的<a href="https://zhongjunma.github.io/blog/intro.html"><cite>博客</cite></a></p>
```

显示如下：

<p>小马的<a href="https://zhongjunma.github.io/blog/intro.html"><cite>博客</cite></a></p>

## 缩略语

使用 `<abbr>` 元素包裹缩略语或者缩写，并在 `title` 元素中提供解释，鼠标悬停皆可查看解释。

```html
<p>我在学习 <abbr title="Hyper text Markup Language">HTML</abbr> 的基础知识。</p>
```

显示如下：

<p>我在学习 <abbr title="Hyper text Markup Language">HTML</abbr> 的基础知识。</p>

## 标记联系方式

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

## 上标和下标

```html
<p>x<sub>i</sub>，y<sup>j</sup></p>
```

显示如下：

<p>x<sub>i</sub>，y<sup>j</sup></p>

## 代码

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

## 标记时间和日期

`<time>` 元素提供了可供机器识别的时间日期格式，并不会展示在界面上。当然，`datetime` 的有很多种可被机器识别的格式。

```html
<time datetime="2021-06-22">2021年6月22日</time> 
```

显示如下：

<time datetime="2021-06-22">2021年6月22日</time> 
