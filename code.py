# PiPi-keyboard – Raspberry Pi PICO ported for KMK revision 
# The original file is here – https://git.40percent.club/di0ib/Misc/src/branch/master/PiPi%20Gherkin/code.py
import board

from kmk.keys import KC, KeyboardKey
# import kmk.extensions.keymap_extras.keymap_jp

from kmk.kmk_keyboard import KMKKeyboard
from kmk.scanners import DiodeOrientation
from kmk.hid import HIDModes

from kmk.modules.layers import Layers
from kmk.modules.holdtap import HoldTap

keyboard = KMKKeyboard()

# モジュールの追加
holdtap = HoldTap() # HoldTapモジュール
layers_ext = Layers() # Layersモジュール
keyboard.modules = [layers_ext, holdtap]
#keyboard.modules.append(Layers())
#keyboard.modules.append(HoldTap())


# 列ピンの定義
keyboard.col_pins = (board.GP2, board.GP3, board.GP4, board.GP5, board.GP6, board.GP7)
# 行ピンの定義
keyboard.row_pins = (board.GP8, board.GP9, board.GP10, board.GP11, board.GP12)
# USBコネクタを右向きにしたい場合は、行・列のピンの順序を反転してキー配列を180度回転する
# keyboard.col_pins = tuple(reversed(keyboard.col_pins))
# keyboard.row_pins = tuple(reversed(keyboard.row_pins))
# ダイオードの方向 = 列→行
keyboard.diode_orientation = DiodeOrientation.COLUMNS
# デバッグ無効 (Trueにするとターミナルにデバッグメッセージが出力される)
from kmk.kmk_keyboard import debug
debug.enabled = False
# keyboard.debug_enabled = False


# Manually define missing JIS keys
KC.INT1 = KeyboardKey(code=135) # Ro
KC.INT3 = KeyboardKey(code=137) # Yen
KC.JP_ZKHK = KeyboardKey(code=53)  # Zenkaku/Hankaku (Grave / Esc)
KC.JP_KANA = KeyboardKey(code=136) # Katakana/Hiragana
KC.JP_MHEN = KeyboardKey(code=139) # Muhenkan
KC.JP_HENK = KeyboardKey(code=138) # Henkan

# JIS Key Definitions
KC.JP_EQL = KC.LSFT(KC.MINS)  # = (Shift + -)
KC.JP_LBRC = KC.RBRC          # [ (US ] key acts as [ on JIS)
KC.JP_RBRC = KC.BSLS          # ] (US \ key acts as ] on JIS)
KC.JP_BSLS = KC.INT3          # \ (Yen key)
KC.JP_UNDS = KC.LSFT(KC.INT1) # _ (Shift + Ro)
KC.JP_PLUS = KC.LSFT(KC.SCLN) # + (Shift + ;)
KC.JP_LCBR = KC.LSFT(KC.RBRC) # { (Shift + US ] key)
KC.JP_RCBR = KC.LSFT(KC.BSLS) # } (Shift + US \ key)
KC.JP_PIPE = KC.LSFT(KC.INT3) # | (Shift + Yen)
KC.JP_QUES = KC.LSFT(KC.SLSH) # ? (Shift + /)
KC.JP_SLSH = KC.SLSH          # /
KC.JP_QUOT = KC.LSFT(KC.N7)   # ' (Shift + 7)
KC.JP_COLN = KC.QUOT          # : (US ' key acts as : on JIS)
KC.JP_DQUO = KC.LSFT(KC.N2)   # " (Shift + 2)

# JIS Layer 2 Symbols
KC.JP_AT = KC.LBRC            # @
KC.JP_CIRC = KC.EQL           # ^
KC.JP_AMPR = KC.LSFT(KC.N6)   # &
KC.JP_ASTR = KC.LSFT(KC.QUOT) # * (Shift + :)
KC.JP_LPRN = KC.LSFT(KC.N8)   # (
KC.JP_RPRN = KC.LSFT(KC.N9)   # )
KC.JP_GRV = KC.LSFT(KC.LBRC)  # ` (Shift + @)

keyboard.keymap = [
    [ # デフォルトのレイヤ (レイヤ0)
        KC.Q, KC.W, KC.E, KC.R, KC.T, KC.Y, KC.U, KC.I, KC.O, KC.P,
        KC.A, KC.S, KC.D, KC.F, KC.G, KC.H, KC.J, KC.K, KC.L, KC.ESC,
        KC.HT(KC.Z, KC.LCTRL), KC.HT(KC.X, KC.LALT), KC.LT(3, KC.C), KC.LT(4, KC.V), KC.LT(2, KC.BSPC),
        KC.LT(1, KC.SPC), KC.LT(5, KC.B), KC.HT(KC.N, KC.RALT), KC.HT(KC.M, KC.RCTRL), KC.HT(KC.ENT, KC.RSFT),
    ],
    [ # レイヤ1
        KC.N1, KC.N2, KC.N3, KC.N4, KC.N5, KC.N6, KC.N7, KC.N8, KC.N9, KC.N0,
        KC.F1, KC.F2, KC.F3, KC.F4, KC.F5, KC.F6, KC.F7, KC.F8, KC.F9, KC.F10,
        KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.DEL, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS,
    ],
    [ # レイヤ2
        KC.EXLM, KC.JP_AT, KC.HASH, KC.DLR, KC.PERC, KC.JP_CIRC, KC.JP_AMPR, KC.JP_ASTR, KC.JP_LPRN, KC.JP_RPRN,
        KC.F11, KC.F12, KC.CAPS, KC.INS, KC.PSCR, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.JP_GRV,
        KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.LGUI, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS,
    ],
    [ # レイヤ3
        KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.MINS, KC.JP_EQL, KC.JP_LBRC, KC.JP_RBRC, KC.JP_BSLS,
        KC.TAB, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.COMM, KC.DOT, KC.JP_SLSH, KC.SCLN, KC.JP_QUOT,
        KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.LEFT, KC.DOWN, KC.UP, KC.RGHT,
    ],
    [ # レイヤ4
        KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.JP_UNDS, KC.JP_PLUS, KC.JP_LCBR, KC.JP_RCBR, KC.JP_PIPE,
        KC.TAB, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.LABK, KC.RABK, KC.JP_QUES, KC.JP_COLN, KC.JP_DQUO,
        KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.HOME, KC.PGDN, KC.PGUP, KC.END,
    ],
    [ # レイヤ5
        KC.JP_ZKHK, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS,
        KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS,
        KC.JP_KANA, KC.JP_MHEN, KC.JP_HENK, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.ENT,
    ],
]

if __name__ == '__main__':
    keyboard.go(hid_type=HIDModes.USB) # USB HID有効
