(html-hyperlink-label)=
# 超链接

## 什么是超链接？

超链接（hyperlink），是允许我们同其他网页或站点之间进行链接的元素。

## `<a>` 元素

可以将文本转化为链接

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
    <a href="https://www.mozilla.org/zh-CN/about/manifesto/" title="了解 Mozilla 的使命">
        Mozilla 宣言
    </a>
    的超链接
</p>

`<a>` 元素指的是 **a**nchor（锚点），属性 `href` 指的是 **h**ypertext **ref**erence（超文本引用），`href` 的值就是网址的链接，属性 `title` 是链接的标题，当鼠标悬停到超链接上时，就会显示 `title` 的值，元素的内容是变为超链接的文本。

```{note}
注意区分元素属性 `title` 以及元素的内容，`title` 是鼠标悬停时的文字，元素的内容始终显示在页面上。
```

同样地，也可以将块级元素转化为块级链接。例如，我们将图像转化为链接。

```html
<a href="https://www.mozilla.org/zh-CN/about/manifesto/" title="了解 Mozilla 的使命">
    <img src="../../images/asuka.png" alt="明日香">
</a>
```

显示如下：

<a href="https://www.mozilla.org/zh-CN/about/manifesto/" title="了解 Mozilla 的使命">
    <img src="../../_images/asuka.png" alt="明日香">
</a>
