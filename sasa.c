/*
 * MySDOS Micro-Kernel v0.1
 * Created by: Louis (Dumai, Indonesia)
 * Written on: iQOO Z10 5G
 * Misi: Menampilkan teks ke layar VGA (Mode Teks)
 */

void kernel_main() {
    // Alamat memori video untuk layar teks VGA (biasanya 0xB8000)
    // Kita pakai 'volatile' agar compiler tidak mengacak-acak urutannya.
    volatile char* video_memory = (volatile char*)0xB8000;

    // Teks yang akan kita tampilkan
    const char* message = "Hello, MySDOS Kernel! - by Louis";

    // Warna teks (Putih di atas Hitam)
    // Di VGA, setiap karakter butuh 2 byte: [Karakter] [Warna]
    char color = 0x07; // 0x07 = Light Grey on Black

    // Loop untuk menulis setiap karakter ke memori video
    int i = 0;
    while (message[i] != '\0') {
        // Tulis karakter ke memori
        video_memory[i * 2] = message[i];
        
        // Tulis atribut warna ke byte berikutnya
        video_memory[i * 2 + 1] = color;
        
        i++;
    }

    // Kernel sudah selesai tugasnya, sekarang kita "Halt" CPU
    // agar tidak melakukan hal aneh-aneh.
    // Di C, kita pakai loop abadi. Di Assembly nanti pakai 'hlt'.
    while (1);
}
