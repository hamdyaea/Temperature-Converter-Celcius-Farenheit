#!/usr/bin/env python3
# Developer: Hamdy Abou El Anein
# Contact: info@daylightlinux.ch
# SPDX-License-Identifier: GPL-3.0-or-later
"""Convert Celsius and Fahrenheit with an accessible Tkinter desktop app."""
from __future__ import annotations
import argparse
import math
import tkinter as tk


def celsius_to_fahrenheit(value: float) -> float:
    if not math.isfinite(value):
        raise ValueError("Temperature must be finite")
    return value * 9 / 5 + 32


def fahrenheit_to_celsius(value: float) -> float:
    if not math.isfinite(value):
        raise ValueError("Temperature must be finite")
    return (value - 32) * 5 / 9


class ConverterApp(tk.Tk):
    def __init__(self) -> None:
        super().__init__()
        self.title("Temperature Converter · Hamdy Abou El Anein")
        self.geometry("450x360")
        self.minsize(380, 310)
        self.configure(bg="#101827")
        self.value = tk.StringVar()
        self.direction = tk.StringVar(value="Celsius → Fahrenheit")
        self.result = tk.StringVar(value="Enter a temperature.")
        box = tk.Frame(self, bg="#101827", padx=30, pady=25)
        box.pack(expand=True, fill="both")
        tk.Label(box, text="TEMPERATURE CONVERTER", bg="#101827", fg="#8bd6c1",
                 font=("DejaVu Sans", 13, "bold")).pack(pady=12)
        tk.OptionMenu(box, self.direction, "Celsius → Fahrenheit",
                      "Fahrenheit → Celsius").pack(pady=10)
        tk.Entry(box, textvariable=self.value, justify="center",
                 font=("DejaVu Sans", 20), width=14).pack(pady=8)
        tk.Label(box, textvariable=self.result, bg="#101827", fg="#f2c879",
                 font=("DejaVu Sans", 18, "bold")).pack(pady=15)
        tk.Button(box, text="Convert", command=self.convert, bg="#7ddcc0",
                  fg="#10211c", relief="flat", padx=25, pady=10).pack(pady=8)
        self.bind("<Return>", lambda _event: self.convert())

    def convert(self) -> None:
        try:
            value = float(self.value.get().strip())
            if self.direction.get().startswith("Celsius"):
                converted = celsius_to_fahrenheit(value)
                unit = "°F"
            else:
                converted = fahrenheit_to_celsius(value)
                unit = "°C"
            self.result.set(f"{converted:.2f} {unit}")
        except ValueError:
            self.result.set("Enter a valid finite number.")


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--celsius", type=float)
    parser.add_argument("--fahrenheit", type=float)
    args = parser.parse_args()
    if args.celsius is not None and args.fahrenheit is not None:
        parser.error("Choose only one conversion direction")
    if args.celsius is not None:
        print(f"{celsius_to_fahrenheit(args.celsius):.2f} °F")
    elif args.fahrenheit is not None:
        print(f"{fahrenheit_to_celsius(args.fahrenheit):.2f} °C")
    else:
        ConverterApp().mainloop()


if __name__ == "__main__":
    main()
