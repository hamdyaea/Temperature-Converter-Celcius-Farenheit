# Developer: Hamdy Abou El Anein
# Contact: info@daylightlinux.ch
# SPDX-License-Identifier: GPL-3.0-or-later
import importlib.util
from pathlib import Path
import unittest
spec=importlib.util.spec_from_file_location("application",Path(__file__).resolve().parents[1]/"TempConverter.py")
app=importlib.util.module_from_spec(spec)
spec.loader.exec_module(app)
class Tests(unittest.TestCase):
    def test_conversions(self):
        self.assertEqual(app.celsius_to_fahrenheit(0),32)
        self.assertEqual(app.fahrenheit_to_celsius(212),100)
        self.assertAlmostEqual(app.celsius_to_fahrenheit(-40),-40)
    def test_invalid(self):
        with self.assertRaises(ValueError):app.celsius_to_fahrenheit(float("inf"))
    def test_gui(self):
        win=app.ConverterApp()
        try:
            win.value.set("100")
            win.convert()
            self.assertEqual(win.result.get(),"212.00 °F")
        finally:win.destroy()

if __name__=="__main__":unittest.main()
