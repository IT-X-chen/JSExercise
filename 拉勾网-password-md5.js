


var window = this;

!function(c) {
    "use strict";
    function a(c, a) {
        var h = (65535 & c) + (65535 & a)
          , d = (c >> 16) + (a >> 16) + (h >> 16);
        return d << 16 | 65535 & h
    }
    function h(c, a) {
        return c << a | c >>> 32 - a
    }
    function d(c, d, e, f, g, v) {
        return a(h(a(a(d, c), a(f, v)), g), e)
    }
    function e(c, a, h, e, f, g, v) {
        return d(a & h | ~a & e, c, a, f, g, v)
    }
    function f(c, a, h, e, f, g, v) {
        return d(a & e | h & ~e, c, a, f, g, v)
    }
    function g(c, a, h, e, f, g, v) {
        return d(a ^ h ^ e, c, a, f, g, v)
    }
    function v(c, a, h, e, f, g, v) {
        return d(h ^ (a | ~e), c, a, f, g, v)
    }
    function i(c, h) {
        c[h >> 5] |= 128 << h % 32,
        c[(h + 64 >>> 9 << 4) + 14] = h;
        var d, i, C, A, l, m = 1732584193, n = -271733879, o = -1732584194, p = 271733878;
        for (d = 0; d < c.length; d += 16)
            i = m,
            C = n,
            A = o,
            l = p,
            m = e(m, n, o, p, c[d], 7, -680876936),
            p = e(p, m, n, o, c[d + 1], 12, -389564586),
            o = e(o, p, m, n, c[d + 2], 17, 606105819),
            n = e(n, o, p, m, c[d + 3], 22, -1044525330),
            m = e(m, n, o, p, c[d + 4], 7, -176418897),
            p = e(p, m, n, o, c[d + 5], 12, 1200080426),
            o = e(o, p, m, n, c[d + 6], 17, -1473231341),
            n = e(n, o, p, m, c[d + 7], 22, -45705983),
            m = e(m, n, o, p, c[d + 8], 7, 1770035416),
            p = e(p, m, n, o, c[d + 9], 12, -1958414417),
            o = e(o, p, m, n, c[d + 10], 17, -42063),
            n = e(n, o, p, m, c[d + 11], 22, -1990404162),
            m = e(m, n, o, p, c[d + 12], 7, 1804603682),
            p = e(p, m, n, o, c[d + 13], 12, -40341101),
            o = e(o, p, m, n, c[d + 14], 17, -1502002290),
            n = e(n, o, p, m, c[d + 15], 22, 1236535329),
            m = f(m, n, o, p, c[d + 1], 5, -165796510),
            p = f(p, m, n, o, c[d + 6], 9, -1069501632),
            o = f(o, p, m, n, c[d + 11], 14, 643717713),
            n = f(n, o, p, m, c[d], 20, -373897302),
            m = f(m, n, o, p, c[d + 5], 5, -701558691),
            p = f(p, m, n, o, c[d + 10], 9, 38016083),
            o = f(o, p, m, n, c[d + 15], 14, -660478335),
            n = f(n, o, p, m, c[d + 4], 20, -405537848),
            m = f(m, n, o, p, c[d + 9], 5, 568446438),
            p = f(p, m, n, o, c[d + 14], 9, -1019803690),
            o = f(o, p, m, n, c[d + 3], 14, -187363961),
            n = f(n, o, p, m, c[d + 8], 20, 1163531501),
            m = f(m, n, o, p, c[d + 13], 5, -1444681467),
            p = f(p, m, n, o, c[d + 2], 9, -51403784),
            o = f(o, p, m, n, c[d + 7], 14, 1735328473),
            n = f(n, o, p, m, c[d + 12], 20, -1926607734),
            m = g(m, n, o, p, c[d + 5], 4, -378558),
            p = g(p, m, n, o, c[d + 8], 11, -2022574463),
            o = g(o, p, m, n, c[d + 11], 16, 1839030562),
            n = g(n, o, p, m, c[d + 14], 23, -35309556),
            m = g(m, n, o, p, c[d + 1], 4, -1530992060),
            p = g(p, m, n, o, c[d + 4], 11, 1272893353),
            o = g(o, p, m, n, c[d + 7], 16, -155497632),
            n = g(n, o, p, m, c[d + 10], 23, -1094730640),
            m = g(m, n, o, p, c[d + 13], 4, 681279174),
            p = g(p, m, n, o, c[d], 11, -358537222),
            o = g(o, p, m, n, c[d + 3], 16, -722521979),
            n = g(n, o, p, m, c[d + 6], 23, 76029189),
            m = g(m, n, o, p, c[d + 9], 4, -640364487),
            p = g(p, m, n, o, c[d + 12], 11, -421815835),
            o = g(o, p, m, n, c[d + 15], 16, 530742520),
            n = g(n, o, p, m, c[d + 2], 23, -995338651),
            m = v(m, n, o, p, c[d], 6, -198630844),
            p = v(p, m, n, o, c[d + 7], 10, 1126891415),
            o = v(o, p, m, n, c[d + 14], 15, -1416354905),
            n = v(n, o, p, m, c[d + 5], 21, -57434055),
            m = v(m, n, o, p, c[d + 12], 6, 1700485571),
            p = v(p, m, n, o, c[d + 3], 10, -1894986606),
            o = v(o, p, m, n, c[d + 10], 15, -1051523),
            n = v(n, o, p, m, c[d + 1], 21, -2054922799),
            m = v(m, n, o, p, c[d + 8], 6, 1873313359),
            p = v(p, m, n, o, c[d + 15], 10, -30611744),
            o = v(o, p, m, n, c[d + 6], 15, -1560198380),
            n = v(n, o, p, m, c[d + 13], 21, 1309151649),
            m = v(m, n, o, p, c[d + 4], 6, -145523070),
            p = v(p, m, n, o, c[d + 11], 10, -1120210379),
            o = v(o, p, m, n, c[d + 2], 15, 718787259),
            n = v(n, o, p, m, c[d + 9], 21, -343485551),
            m = a(m, i),
            n = a(n, C),
            o = a(o, A),
            p = a(p, l);
        return [m, n, o, p]
    }
    function C(c) {
        var a, h = "";
        for (a = 0; a < 32 * c.length; a += 8)
            h += String.fromCharCode(c[a >> 5] >>> a % 32 & 255);
        return h
    }
    function A(c) {
        var a, h = [];
        for (h[(c.length >> 2) - 1] = void 0,
        a = 0; a < h.length; a += 1)
            h[a] = 0;
        for (a = 0; a < 8 * c.length; a += 8)
            h[a >> 5] |= (255 & c.charCodeAt(a / 8)) << a % 32;
        return h
    }
    function l(c) {
        return C(i(A(c), 8 * c.length))
    }
    function m(c, a) {
        var h, d, e = A(c), f = [], g = [];
        for (f[15] = g[15] = void 0,
        e.length > 16 && (e = i(e, 8 * c.length)),
        h = 0; 16 > h; h += 1)
            f[h] = 909522486 ^ e[h],
            g[h] = 1549556828 ^ e[h];
        return d = i(f.concat(A(a)), 512 + 8 * a.length),
        C(i(g.concat(d), 640))
    }
    function n(c) {
        var a, h, d = "0123456789abcdef", e = "";
        for (h = 0; h < c.length; h += 1)
            a = c.charCodeAt(h),
            e += d.charAt(a >>> 4 & 15) + d.charAt(15 & a);
        return e
    }
    function o(c) {
        return unescape(encodeURIComponent(c))
    }
    function p(c) {
        return l(o(c))
    }
    function q(c) {
        return n(p(c))
    }
    function r(c, a) {
        return m(o(c), o(a))
    }
    function s(c, a) {
        return n(r(c, a))
    }
    function t(c, a, h) {
        return a ? h ? r(a, c) : s(a, c) : h ? p(c) : q(c)
    }
    "function" == typeof define && define.amd ? define("common/widgets/passport/dep/md5/md5", ["require"], function() {
        return t
    }) : window.md5 = t
}(this);
md5 = window.md5;


var password = "123456",
v="veenike"
password = md5(password);
password = md5(v +password + v);
console.log(password);