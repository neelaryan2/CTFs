

;
; +-------------------------------------------------------------------------+
; |      This file was generated by The Interactive Disassembler (IDA)      |
; |           Copyright (c) 2020 Hex-Rays, <support@hex-rays.com>           |
; |                      License info: 48-174E-39B0-5F                      |
; |          Hex-Rays SA. 【請支持正版】, Unlimited License          |
; +-------------------------------------------------------------------------+
;
; Input SHA256 : FDED7B6B7BF72D491C1678EA11F84AEEEF117399C9D2B53D8DC02EBAEB5ADCB9
; Input MD5    : EBE69994EA596500C78C34383A810C71
; Input CRC32  : D8C08A3E

; File Name   : C:\Users\Neel\Downloads\CSAW_finals_2021\imports\code.bin
; Format      : Binary file
; Base Address: 0000h Range: 0000h - 0228h Loaded length: 0228h

                .686p
                .mmx
                .model flat

; ===========================================================================

; Segment type: Pure code
seg000          segment byte public 'CODE' use32
                assume cs:seg000
                assume es:nothing, ss:nothing, ds:nothing, fs:nothing, gs:nothing
                db 0E8h
                db 39h, 2 dup(0)
                dd 0Bh dup(0)
dword_30        dd 0                    ; DATA XREF: sub_3E+F↓r
                dd 22960100h, 0AEFADEF7h
                db 0D2h, 0B1h

; =============== S U B R O U T I N E =======================================

; Attributes: noreturn fuzzy-sp

sub_3E          proc near

; FUNCTION CHUNK AT 00000220 SIZE 00000008 BYTES

                pop     edx
                mov     esp, edx
                sub     esp, 100h
                and     esp, 0FFFFFF00h
                mov     ecx, fs:dword_30
                test    ecx, ecx
                jz      loc_220
                cmp     byte ptr [ecx+2], 0
                jnz     loc_87
                mov     ecx, [ecx+0Ch]
                test    ecx, ecx
                jz      loc_220
                mov     ebx, [ecx+14h]
                test    ebx, ebx
                jz      loc_220
                add     ecx, 14h
                cmp     ecx, ebx
                jz      loc_220

loc_87:                                 ; CODE XREF: sub_3E+22↑j
                                        ; sub_3E+70↓j
                push    dword ptr [ebx+28h]
                call    sub_134
                add     esp, 4
                push    edx
                call    sub_E9
                add     esp, 4
                cmp     eax, [edx+31h]
                jz      loc_B3
                mov     ebx, [ebx]
                cmp     ecx, ebx
                jz      loc_220
                jmp     loc_87
; ---------------------------------------------------------------------------

loc_B3:                                 ; CODE XREF: sub_3E+60↑j
                mov     ebx, [ebx+10h]
                movzx   ecx, byte ptr [edx+30h]

loc_BA:                                 ; CODE XREF: sub_3E+9B↓j
                mov     edi, edx
                add     edi, 31h ; '1'
                add     edi, ecx
                add     edi, ecx
                add     edi, ecx
                add     edi, ecx
                mov     esi, [edi]
                push    esi
                push    ebx
                call    sub_15E
                add     esp, 8
                mov     [edi], eax
                dec     ecx
                cmp     ecx, 0
                jnz     loc_BA
                call    sub_20F
                jmp     loc_220
sub_3E          endp


; =============== S U B R O U T I N E =======================================

; Attributes: bp-based frame

sub_E9          proc near               ; CODE XREF: sub_3E+55↑p
                                        ; sub_15E+77↓p

var_4           = dword ptr -4
arg_0           = dword ptr  8

                push    ebp
                mov     ebp, esp
                pusha
                mov     ecx, [ebp+arg_0]
                xor     edx, edx
                xor     eax, eax

loc_F4:                                 ; CODE XREF: sub_E9+2C↓j
                movsx   esi, byte ptr [ecx]
                test    esi, esi
                jz      loc_11A
                add     esi, edx
                mov     edi, esi
                shl     edi, 5
                shl     edi, 5
                add     edi, esi
                mov     edx, edi
                shr     edx, 5
                shr     edx, 1
                xor     edx, edi
                inc     ecx
                jmp     loc_F4
; ---------------------------------------------------------------------------

loc_11A:                                ; CODE XREF: sub_E9+10↑j
                lea     eax, [edx+edx*8]
                mov     ecx, eax
                shr     ecx, 0Bh
                xor     ecx, eax
                mov     eax, ecx
                shl     eax, 0Fh
                add     eax, ecx
                mov     [esp+20h+var_4], eax
                popa
                mov     esp, ebp
                pop     ebp
                retn
sub_E9          endp


; =============== S U B R O U T I N E =======================================

; Attributes: bp-based frame

sub_134         proc near               ; CODE XREF: sub_3E+4C↑p

arg_0           = dword ptr  8

                push    ebp
                mov     ebp, esp
                pusha
                mov     esi, [ebp+arg_0]
                xor     ecx, ecx

loc_13D:                                ; CODE XREF: sub_134+1D↓j
                mov     ax, [esi]
                test    ax, ax
                jz      loc_156
                or      al, 20h
                mov     [edx], al
                add     esi, 2
                inc     edx
                jmp     loc_13D
; ---------------------------------------------------------------------------

loc_156:                                ; CODE XREF: sub_134+F↑j
                mov     byte ptr [edx], 0
                popa
                mov     esp, ebp
                pop     ebp
                retn
sub_134         endp


; =============== S U B R O U T I N E =======================================

; Attributes: bp-based frame

sub_15E         proc near               ; CODE XREF: sub_3E+8D↑p

var_38          = dword ptr -38h
var_34          = dword ptr -34h
var_30          = dword ptr -30h
var_2C          = dword ptr -2Ch
var_4           = dword ptr -4
arg_0           = dword ptr  8
arg_4           = dword ptr  0Ch

                push    ebp
                mov     ebp, esp
                pusha
                sub     esp, 18h
                mov     edi, [ebp+arg_0]
                test    edi, edi
                jz      loc_201
                mov     edx, [ebp+arg_4]
                mov     ecx, [edi+3Ch]
                mov     eax, [ecx+edi+78h]
                test    eax, eax
                jz      loc_201
                cmp     dword ptr [ecx+edi+7Ch], 0
                jz      loc_201
                lea     ecx, [eax+edi]
                mov     [esp+38h+var_38], ecx
                mov     ecx, [eax+edi+1Ch]
                add     ecx, edi
                mov     [esp+38h+var_34], ecx
                mov     ecx, [eax+edi+20h]
                add     ecx, edi
                mov     [esp+38h+var_30], ecx
                mov     ecx, [eax+edi+24h]
                add     ecx, edi
                mov     [esp+38h+var_2C], ecx
                mov     eax, [esp+38h+var_38]
                cmp     dword ptr [eax+18h], 0
                jz      loc_201
                xor     ebx, ebx

loc_1C0:                                ; CODE XREF: sub_15E+9E↓j
                mov     eax, [esp+38h+var_30]
                mov     ecx, [eax+ebx*4]
                cmp     byte ptr [ecx+edi], 0
                jz      loc_1FB
                lea     eax, [ecx+edi]
                push    eax
                call    sub_E9
                add     esp, 4
                cmp     eax, edx
                jnz     loc_1FB
                mov     eax, [esp+38h+var_2C]
                movzx   ecx, word ptr [eax+ebx*2]
                mov     eax, [esp+38h+var_34]
                mov     eax, [eax+ecx*4]
                add     eax, edi
                jmp     loc_203
; ---------------------------------------------------------------------------

loc_1FB:                                ; CODE XREF: sub_15E+6D↑j
                                        ; sub_15E+81↑j
                inc     ebx
                jmp     loc_1C0
; ---------------------------------------------------------------------------

loc_201:                                ; CODE XREF: sub_15E+C↑j
                                        ; sub_15E+1E↑j ...
                xor     eax, eax

loc_203:                                ; CODE XREF: sub_15E+98↑j
                add     esp, 18h
                mov     [esp+20h+var_4], eax
                popa
                mov     esp, ebp
                pop     ebp
                retn
sub_15E         endp


; =============== S U B R O U T I N E =======================================

; Attributes: bp-based frame

sub_20F         proc near               ; CODE XREF: sub_3E+A1↑p

var_4           = dword ptr -4

                push    ebp
                mov     ebp, esp
                pusha
                push    edx
                call    dword ptr [edx+35h]
                mov     [esp+20h+var_4], eax
                popa
                mov     esp, ebp
                pop     ebp
                retn
sub_20F         endp

; ---------------------------------------------------------------------------
; START OF FUNCTION CHUNK FOR sub_3E

loc_220:                                ; CODE XREF: sub_3E+18↑j
                                        ; sub_3E+2D↑j ...
                nop
                nop
                nop
                nop
                nop
                nop
                nop
                nop
; END OF FUNCTION CHUNK FOR sub_3E
seg000          ends


                end
