// ==========================================
// boot.s - MySDOS Mobile 64-Bit Bootloader
// Developed by: Louis (Dumai Symmetrical)
// ==========================================

.section ".text.boot"    // Bagian ini akan ditaruh paling awal di RAM
.global _start           // Titik masuk utama OS

_start:
    // 1. CEK CORE CPU
    // HP iQOO punya banyak core (Octa-core). Kita cuma butuh satu (Core 0).
    // Baca ID Processor ke register x0
    mrs     x0, mpidr_el1
    and     x0, x0, #0xFF        // Ambil 8 bit terakhir (ID Core)
    cbz     x0, master           // Jika ID-nya 0, lanjut ke 'master'
    
    // 2. CORE LAIN (Core 1-7) HARUS TIDUR
halt:
    wfe                          // Wait For Event (Hemat baterai!)
    b       halt                 // Loop selamanya kalau bangun lagi

master:
    // 3. SETUP STACK POINTER (SP)
    // Supaya bahasa C bisa kerja (buat simpan variabel sementara),
    // kita butuh Stack. Kita arahkan SP ke alamat awal kode kita.
    ldr     x0, =_start
    mov     sp, x0

    // 4. BERSIHKAN BSS (Zero out BSS section)
    // Menghapus data sampah di RAM supaya variabel C mulai dari nol.
    ldr     x1, =__bss_start
    ldr     w2, =__bss_size
setup_bss:
    cbz     w2, jump_to_kernel   // Jika BSS kosong atau sudah habis, lompat
    str     xzr, [x1], #8        // Isi dengan nol (xzr = zero register)
    sub     w2, w2, #1
    cbnz    w2, setup_bss

jump_to_kernel:
    // 5. PANGGIL KERNEL C
    // Sekarang CPU sudah siap, panggil fungsi 'main' di kernel.c
    bl      main

    // Jika kernel.c selesai (seharusnya tidak), balik ke halt
    b       halt
