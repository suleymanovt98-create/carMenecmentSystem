🚗 Avtomobil İdarəetmə Sistemi

Python ilə yazılmış konsol proqramı. Menyuda ox düymələri ilə gəzirsən, Enter ilə seçirsən. Maşın əlavə et, bütün maşınlara bax, yenilə, sil və filtrlə. 🏁

✨ Nələr edə bilir?
Menyu bəndi	Funksiya	Nə edir?
➕ Add Car	addCar()	Yeni maşın əlavə edir
📋 Show All Cars	showAllCars()	Bütün maşınları göstərir
✏️ Update Car	updateCar()	Mövcud maşının məlumatını dəyişir
🗑️ Delete Car	deleteCar()	Maşını silir
🔍 Filter Cars	filterCars()	Maşınları şərtə görə süzgəcdən keçirir
🚪 Exit	,	Proqramdan çıxır
🎮 İdarəetmə
Düymə	Hərəkət
⬆️ Yuxarı ox	Bir bənd yuxarı
⬇️ Aşağı ox	Bir bənd aşağı
⏎ Enter	Seçilmiş bəndi işə sal

Seçilmiş bənd ekranda --> işarəsi ilə göstərilir:

$$$$$$ WELCOME CAR MANAGEMENT $$$$$$

     Add Car
 --> Show All Cars
     Update Car
     Delete Car
     Filter Cars
     Exit

Menyu dövri işləyir: ən yuxarıda yuxarı ox basanda ən aşağıya, ən aşağıda aşağı ox basanda ən yuxarıya keçir. 🔄

Hər əməliyyatdan sonra Press Enter to continue... yazısı çıxır və Enter basanda menyuya qayıdırsan.

📁 Layihənin strukturu
📦 car-project
 ┣ 📜 main.py     → menyu (ox düymələri ilə idarə)
 ┗ 📜 cars.py     → maşınlarla bağlı bütün funksiyalar
Menyu faylı yalnız istifadəçi interfeysi ilə işləyir: ekranı təmizləyir, seçimi göstərir, düymələri oxuyur.
cars.py əsas işi görür: addCar, showAllCars, updateCar, deleteCar, filterCars.
🚀 Necə işə salmaq olar?
Python 3 quraşdırılmış olmalıdır:
   python --version
Hər iki faylı eyni qovluğa qoy.
Terminalda həmin qovluğa keç və menyu faylını işə sal:
   python main.py

Əlavə kitabxana quraşdırmaq lazım deyil. Yalnız Python-un daxili modulları (os, msvcrt) istifadə olunur. 🎉

⚠️ Vacib qeyd: yalnız Windows!

Proqram Windows üçün yazılıb:

msvcrt modulu yalnız Windows-da var, düymə basılmasını gözləmək üçün istifadə olunur.
os.system("cls") ekranı təmizləyir. Bu əmr də Windows-a aiddir (Linux və macOS-da clear olur).

Linux/macOS-da işlətmək istəsən, bu hissələri başqa üsulla əvəz etmək lazımdır.

🧠 Menyu necə işləyir?
selected dəyişəni hazırda hansı bəndin seçildiyini saxlayır.
while True döngüsü hər dəfə ekranı təmizləyib menyunu yenidən çəkir.
msvcrt.getch() basılan düyməni oxuyur:
Ox düymələri iki mərhələdə gəlir: əvvəl b'\xe0', sonra b'H' (yuxarı) və ya b'P' (aşağı).
b'\r' Enter düyməsidir.
% (modul) operatoru sayəsində menyu dövri keçid edir.
Exit seçiləndə break döngünü dayandırır.
🔮 Gələcək planlar (To-Do)
[ ] Rəngli menyu 🎨
[ ] Esc düyməsi ilə çıxış
[ ] Linux/macOS dəstəyi
[ ] Maşınları qiymətə və ilə görə sıralamaq
[ ] Silmədən əvvəl təsdiq sualı
🛠️ İstifadə olunan texnologiyalar
🐍 Python 3
⌨️ msvcrt (düymə oxuma)
🖥️ os (ekranı təmizləmə)

Kod yaz, sına, düzəlt. Hər yeni layihə səni bir addım irəli a
