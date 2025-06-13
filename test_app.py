#!/usr/bin/env python3
import subprocess
import sys

def test_app():
    """Test aplikasi to-do list dengan input '3' untuk keluar"""
    try:
        # Menjalankan aplikasi dengan input '3'
        result = subprocess.run(
            [sys.executable, 'todo_app/main.py'],
            input='3\n',
            text=True,
            capture_output=True,
            timeout=10
        )
        
        print("=== OUTPUT APLIKASI ===")
        print(result.stdout)
        
        if result.stderr:
            print("=== ERROR ===")
            print(result.stderr)
        
        print(f"=== EXIT CODE: {result.returncode} ===")
        
        # Cek apakah aplikasi menampilkan menu dan pesan perpisahan
        output = result.stdout
        if "Selamat Datang di Aplikasi To-Do List" in output:
            print("✓ Menu ditampilkan dengan benar")
        else:
            print("✗ Menu tidak ditampilkan")
            
        if "Terima kasih telah menggunakan aplikasi To-Do List!" in output:
            print("✓ Pesan perpisahan ditampilkan dengan benar")
        else:
            print("✗ Pesan perpisahan tidak ditampilkan")
            
        if result.returncode == 0:
            print("✓ Aplikasi keluar dengan benar")
        else:
            print("✗ Aplikasi tidak keluar dengan benar")
            
    except subprocess.TimeoutExpired:
        print("✗ Aplikasi timeout (mungkin tidak keluar)")
    except Exception as e:
        print(f"✗ Error saat menjalankan test: {e}")

if __name__ == "__main__":
    test_app()