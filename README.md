# 🦈 QR Code STL Generator for Geocaching Trackables

This script generates a 3D-printable STL file of a **reverse (negative) QR code** that links to a specific Geocaching.com trackable using its **tracking code**.

It’s ideal for embedding scannable codes in 3D prints like custom tokens, travel bugs, or shark-shaped chaos coins.

---

## 📦 Dependencies

You’ll need Python 3 and a few libraries:

```bash
pip install segno shapely trimesh numpy mapbox_earcut
```

**Note:** `mapbox_earcut` is required for proper polygon triangulation during extrusion.

---


## 🧠 Who this is for

This script is meant for **makers comfortable with the command line** and basic Python environments.

If you're unfamiliar with:
- running `python` scripts from the terminal,
- installing packages with `pip`,
- or working with 3D files like `.stl`,

If so, this project might not be the best starting point—it's deep nerd magic involving geometry, mesh generation, and QR encoding.

For everyone else:  
Welcome aboard. Let’s make sharks scannable. 🦈✨

---

## 🛠 Usage

```bash
python qr_generator.py TBB5E92
```

- Replace `TBB5E92` with your actual **tracking code**.
- This will generate an STL file named:
  ```
  TBB5E92_qr_inverse_easyprint.stl
  ```

---

## 📎 Notes

- The script uses the short URL format:  
  `geo.co/TBB5E92`  
  which redirects to the full trackable page.

- The QR code is **inverted** (a negative), so it's suitable for filament swapping or multi-color printing — e.g. printing the background first and the QR “holes” in a different color.

- It **only works for active tracking codes that you own** or were issued by Groundspeak. The script does **not fetch or validate** activation status — it’s your responsibility to assign the correct one.

---

## ⚠️ Limitations

- This does **not generate Micro QR Codes** (`micro=False`) to ensure broad phone compatibility.
- Error correction is set to `'L'` (7%) for best balance between scan reliability and printability.
- QR size is determined by the length of the tracking link — short formats like `geo.co/XXXXXXX` help reduce density.

---

## 🐙 License

Do shark things. stay excellent to each other. Attribution appreciated but not required. 🦈

---

***✨ Generated with some help from ChatGPT to automate QR geometry and 3D model generation.***
