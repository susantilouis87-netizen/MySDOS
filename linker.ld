ENTRY(_start)
SECTIONS
{
    /* Alamat 0x40000000 adalah standar RAM untuk ARM64 di QEMU */
    . = 0x40000000;
    .text : { *(.text.boot) *(.text) }
    .data : { *(.data) }
    .bss : {
        . = ALIGN(16);
        __bss_start = .;
        *(.bss)
        __bss_end = .;
    }
    /* Menghitung ukuran BSS untuk dibersihkan di boot.s */
    __bss_size = (__bss_end - __bss_start) >> 3;
}
