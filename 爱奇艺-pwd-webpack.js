
var o, s, b, a = {}, w = {}, k = 65536, C = k - 1, _ = function(e) {
    this.digits = "boolean" == typeof e && !0 === e ? null : o.slice(0),
    this.isNeg = !1
};
function r(e) {
    var t = w
      , i = t.biDivideByRadixPower(e, this.k - 1)
      , i = t.biMultiply(i, this.mu)
      , i = t.biDivideByRadixPower(i, this.k + 1)
      , e = t.biModuloByRadixPower(e, this.k + 1)
      , i = t.biMultiply(i, this.modulus)
      , i = t.biModuloByRadixPower(i, this.k + 1)
      , n = t.biSubtract(e, i);
    n.isNeg && (n = t.biAdd(n, this.bkplus1));
    for (var o = 0 <= t.biCompare(n, this.modulus); o; )
        n = t.biSubtract(n, this.modulus),
        o = 0 <= t.biCompare(n, this.modulus);
    return n
}
function c(e, t) {
    t = w.biMultiply(e, t);
    return this.modulo(t)
}
function d(e, t) {
    var i = new _;
    i.digits[0] = 1;
    for (var n = e, o = t; 0 != (1 & o.digits[0]) && (i = this.multiplyMod(i, n)),
    0 != (o = w.biShiftRight(o, 1)).digits[0] || 0 != w.biHighIndex(o); )
        n = this.multiplyMod(n, n);
    return i
}
a.BarrettMu = function(e) {
    this.modulus = w.biCopy(e),
    this.k = w.biHighIndex(this.modulus) + 1;
    e = new _;
    e.digits[2 * this.k] = 1,
    this.mu = w.biDivide(e, this.modulus),
    this.bkplus1 = new _,
    this.bkplus1.digits[this.k + 1] = 1,
    this.modulo = r,
    this.multiplyMod = c,
    this.powMod = d
}
,
w.biModuloByRadixPower = function(e, t) {
    var i = new _;
    return w.arrayCopy(e.digits, 0, i.digits, 0, t),
    i
}
,
w.biMultiply = function(e, t) {
    for (var i, n, o, s = new _, a = w.biHighIndex(e), r = w.biHighIndex(t), c = 0; c <= r; ++c) {
        for (o = c,
        j = i = 0; j <= a; ++j,
        ++o)
            n = s.digits[o] + e.digits[j] * t.digits[c] + i,
            s.digits[o] = n & C,
            i = n >>> 16;
        s.digits[c + a + 1] = i
    }
    return s.isNeg = e.isNeg != t.isNeg,
    s
}
,
w.biDivideByRadixPower = function(e, t) {
    var i = new _;
    return w.arrayCopy(e.digits, t, i.digits, 0, i.digits.length - t),
    i
}
,
w.biDivide = function(e, t) {
    return w.biDivideModulo(e, t)[0]
}
,
w.setMaxDigits = function(e) {
    o = new Array(e);
    for (var t = 0; t < o.length; t++)
        o[t] = 0;
    s = new _,
    (b = new _).digits[0] = 1
}
,
w.setMaxDigits(20),
w.biCopy = function(e) {
    var t = new _(!0);
    return t.digits = e.digits.slice(0),
    t.isNeg = e.isNeg,
    t
}
,
w.reverseStr = function(e) {
    for (var t = "", i = e.length - 1; -1 < i; --i)
        t += e.charAt(i);
    return t
}
;
var l = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"];
w.biToString = function(e, t) {
    var i = new _;
    i.digits[0] = t;
    for (var n = w.biDivideModulo(e, i), o = l[n[1].digits[0]]; 1 == w.biCompare(n[0], s); )
        n = w.biDivideModulo(n[0], i),
        digit = n[1].digits[0],
        o += l[n[1].digits[0]];
    return (e.isNeg ? "-" : "") + w.reverseStr(o)
}
;
var u = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "a", "b", "c", "d", "e", "f"];
w.digitToHex = function(e) {
    var t = "";
    for (i = 0; i < 4; ++i)
        t += u[15 & e],
        e >>>= 4;
    return w.reverseStr(t)
}
,
w.biToHex = function(e) {
    for (var t = "", i = (w.biHighIndex(e),
    w.biHighIndex(e)); -1 < i; --i)
        t += w.digitToHex(e.digits[i]);
    return t
}
,
w.charToHex = function(e) {
    e = 48 <= e && e <= 57 ? e - 48 : 65 <= e && e <= 90 ? 10 + e - 65 : 97 <= e && e <= 122 ? 10 + e - 97 : 0;
    return e
}
,
w.hexToDigit = function(e) {
    for (var t = 0, i = Math.min(e.length, 4), n = 0; n < i; ++n)
        t <<= 4,
        t |= w.charToHex(e.charCodeAt(n));
    return t
}
,
w.biFromHex = function(e) {
    for (var t = new _, i = e.length, n = 0; 0 < i; i -= 4,
    ++n)
        t.digits[n] = w.hexToDigit(e.substr(Math.max(i - 4, 0), Math.min(i, 4)));
    return t
}
,
w.biAdd = function(e, t) {
    var i;
    if (e.isNeg != t.isNeg)
        t.isNeg = !t.isNeg,
        i = w.biSubtract(e, t),
        t.isNeg = !t.isNeg;
    else {
        i = new _;
        for (var n, o = 0, s = 0; s < e.digits.length; ++s)
            n = e.digits[s] + t.digits[s] + o,
            i.digits[s] = n % k,
            o = Number(k <= n);
        i.isNeg = e.isNeg
    }
    return i
}
,
w.biSubtract = function(e, t) {
    if (e.isNeg != t.isNeg)
        t.isNeg = !t.isNeg,
        n = w.biAdd(e, t),
        t.isNeg = !t.isNeg;
    else {
        for (var i, n = new _, o = 0, s = 0; s < e.digits.length; ++s)
            i = e.digits[s] - t.digits[s] + o,
            n.digits[s] = i % k,
            n.digits[s] < 0 && (n.digits[s] += k),
            o = 0 - Number(i < 0);
        if (-1 == o) {
            for (s = o = 0; s < e.digits.length; ++s)
                i = 0 - n.digits[s] + o,
                n.digits[s] = i % k,
                n.digits[s] < 0 && (n.digits[s] += k),
                o = 0 - Number(i < 0);
            n.isNeg = !e.isNeg
        } else
            n.isNeg = e.isNeg
    }
    return n
}
,
w.biHighIndex = function(e) {
    for (var t = e.digits.length - 1; 0 < t && 0 == e.digits[t]; )
        --t;
    return t
}
,
w.biNumBits = function(e) {
    for (var t = w.biHighIndex(e), i = e.digits[t], n = 16 * (t + 1), o = n; n - 16 < o && 0 == (32768 & i); --o)
        i <<= 1;
    return o
}
,
w.biMultiplyDigit = function(e, t) {
    var i, n, o;
    result = new _,
    i = w.biHighIndex(e);
    for (var s = n = 0; s <= i; ++s)
        o = result.digits[s] + e.digits[s] * t + n,
        result.digits[s] = o & C,
        n = o >>> 16;
    return result.digits[1 + i] = n,
    result
}
,
w.arrayCopy = function(e, t, i, n, o) {
    for (var s = Math.min(t + o, e.length), a = t, r = n; a < s; ++a,
    ++r)
        i[r] = e[a]
}
;
var p = [0, 32768, 49152, 57344, 61440, 63488, 64512, 65024, 65280, 65408, 65472, 65504, 65520, 65528, 65532, 65534, 65535];
w.biShiftLeft = function(e, t) {
    var i = Math.floor(t / 16)
      , n = new _;
    w.arrayCopy(e.digits, 0, n.digits, i, n.digits.length - i);
    for (var o = t % 16, s = 16 - o, a = n.digits.length - 1, r = a - 1; 0 < a; --a,
    --r)
        n.digits[a] = n.digits[a] << o & C | (n.digits[r] & p[o]) >>> s;
    return n.digits[0] = n.digits[a] << o & C,
    n.isNeg = e.isNeg,
    n
}
;
var h = [0, 1, 3, 7, 15, 31, 63, 127, 255, 511, 1023, 2047, 4095, 8191, 16383, 32767, 65535];
w.biShiftRight = function(e, t) {
    var i = Math.floor(t / 16)
      , n = new _;
    w.arrayCopy(e.digits, i, n.digits, 0, e.digits.length - i);
    for (var o = t % 16, s = 16 - o, a = 0, r = a + 1; a < n.digits.length - 1; ++a,
    ++r)
        n.digits[a] = n.digits[a] >>> o | (n.digits[r] & h[o]) << s;
    return n.digits[n.digits.length - 1] >>>= o,
    n.isNeg = e.isNeg,
    n
}
,
w.biMultiplyByRadixPower = function(e, t) {
    var i = new _;
    return w.arrayCopy(e.digits, 0, i.digits, t, i.digits.length - t),
    i
}
,
w.biCompare = function(e, t) {
    if (e.isNeg != t.isNeg)
        return 1 - 2 * Number(e.isNeg);
    for (var i = e.digits.length - 1; 0 <= i; --i)
        if (e.digits[i] != t.digits[i])
            return e.isNeg ? 1 - 2 * Number(e.digits[i] > t.digits[i]) : 1 - 2 * Number(e.digits[i] < t.digits[i]);
    return 0
}
,
w.biDivideModulo = function(e, t) {
    var i, n, o = w.biNumBits(e), s = w.biNumBits(t), a = t.isNeg;
    if (o < s)
        return e.isNeg ? ((i = w.biCopy(b)).isNeg = !t.isNeg,
        e.isNeg = !1,
        t.isNeg = !1,
        n = biSubtract(t, e),
        e.isNeg = !0,
        t.isNeg = a) : (i = new _,
        n = w.biCopy(e)),
        [i, n];
    i = new _,
    n = e;
    for (var r = Math.ceil(s / 16) - 1, c = 0; t.digits[r] < 32768; )
        t = w.biShiftLeft(t, 1),
        ++c,
        ++s,
        r = Math.ceil(s / 16) - 1;
    n = w.biShiftLeft(n, c),
    o += c;
    for (var d = Math.ceil(o / 16) - 1, l = w.biMultiplyByRadixPower(t, d - r); -1 != w.biCompare(n, l); )
        ++i.digits[d - r],
        n = w.biSubtract(n, l);
    for (var u = d; r < u; --u) {
        var p = u >= n.digits.length ? 0 : n.digits[u]
          , h = u - 1 >= n.digits.length ? 0 : n.digits[u - 1]
          , g = u - 2 >= n.digits.length ? 0 : n.digits[u - 2]
          , f = r >= t.digits.length ? 0 : t.digits[r]
          , m = r - 1 >= t.digits.length ? 0 : t.digits[r - 1];
        i.digits[u - r - 1] = p == f ? C : Math.floor((p * k + h) / f);
        for (var v = i.digits[u - r - 1] * (f * k + m), y = 4294967296 * p + (h * k + g); y < v; )
            --i.digits[u - r - 1],
            v = i.digits[u - r - 1] * (f * k | m),
            y = p * k * k + (h * k + g);
        l = w.biMultiplyByRadixPower(t, u - r - 1),
        (n = w.biSubtract(n, w.biMultiplyDigit(l, i.digits[u - r - 1]))).isNeg && (n = w.biAdd(n, l),
        --i.digits[u - r - 1])
    }
    return n = w.biShiftRight(n, c),
    i.isNeg = e.isNeg != a,
    e.isNeg && (i = a ? w.biAdd(i, b) : w.biSubtract(i, b),
    t = w.biShiftRight(t, c),
    n = w.biSubtract(t, n)),
    0 == n.digits[0] && 0 == w.biHighIndex(n) && (n.isNeg = !1),
    [i, n]
}
;
var g = function(e, t, i) {
    var n = w;
    this.e = n.biFromHex(e),
    this.d = n.biFromHex(t),
    this.m = n.biFromHex(i),
    this.chunkSize = 2 * n.biHighIndex(this.m),
    this.radix = 16,
    this.barrett = new a.BarrettMu(this.m)
};
w.getKeyPair = function(e, t, i) {
    return new g(e,t,i)
}
,
w.encryptedString = function(e, t) {
    for (var i = [], n = t.length, o = 0; o < n; )
        i[o] = t.charCodeAt(o),
        o++;
    for (; i.length % e.chunkSize != 0; )
        i[o++] = 0;
    for (var s, a, r, c = i.length, d = "", o = 0; o < c; o += e.chunkSize) {
        for (r = new _,
        s = 0,
        a = o; a < o + e.chunkSize; ++s)
            r.digits[s] = i[a++],
            r.digits[s] += i[a++] << 8;
        var l = e.barrett.powMod(r, e.e);
        d += (16 == e.radix ? w.biToHex(l) : w.biToString(l, e.radix)) + " "
    }
    return d.substring(0, d.length - 1)
}
,
w.setMaxDigits(130);




function rsaFun(e) {
    var t = w.getKeyPair("10001", "", "ab86b6371b5318aaa1d3c9e612a9f1264f372323c8c0f19875b5fc3b3fd3afcc1e5bec527aa94bfa85bffc157e4245aebda05389a5357b75115ac94f074aefcd");
    return w.encryptedString(t, encodeURIComponent(e)).replace(/\s/g, "-");
}

console.log(rsaFun("123456"))