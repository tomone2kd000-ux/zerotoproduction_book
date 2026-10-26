'use client';

import { useState, useEffect } from 'react';
import { BookOpen, Type, Palette } from 'lucide-react';

export function KindleReaderControls() {
  const [theme, setTheme] = useState('cream');
  const [fontSize, setFontSize] = useState('md');
  const [fontFamily, setFontFamily] = useState('serif');

  useEffect(() => {
    const savedTheme = localStorage.getItem('kindle_theme') || 'cream';
    const savedSize = localStorage.getItem('kindle_font_size') || 'md';
    const savedFont = localStorage.getItem('kindle_font_family') || 'serif';

    setTheme(savedTheme);
    setFontSize(savedSize);
    setFontFamily(savedFont);

    applyTheme(savedTheme);
    applyFontSize(savedSize);
    applyFontFamily(savedFont);
  }, []);

  const applyTheme = (val: string) => {
    const html = document.documentElement;
    if (val === 'cream') {
      html.removeAttribute('data-paper-theme');
    } else {
      html.setAttribute('data-paper-theme', val);
    }
  };

  const applyFontSize = (val: string) => {
    const html = document.documentElement;
    html.classList.remove('text-sm', 'text-base', 'text-lg', 'text-xl');
    if (val === 'sm') html.classList.add('text-sm');
    if (val === 'md') html.classList.add('text-base');
    if (val === 'lg') html.classList.add('text-lg');
    if (val === 'xl') html.classList.add('text-xl');
  };

  const applyFontFamily = (val: string) => {
    const html = document.documentElement;
    if (val === 'serif') {
      html.classList.add('font-serif');
      html.classList.remove('font-sans');
    } else {
      html.classList.add('font-sans');
      html.classList.remove('font-serif');
    }
  };

  const handleThemeChange = (newTheme: string) => {
    setTheme(newTheme);
    localStorage.setItem('kindle_theme', newTheme);
    applyTheme(newTheme);
  };

  const handleSizeChange = (newSize: string) => {
    setFontSize(newSize);
    localStorage.setItem('kindle_font_size', newSize);
    applyFontSize(newSize);
  };

  const handleFontChange = (newFont: string) => {
    setFontFamily(newFont);
    localStorage.setItem('kindle_font_family', newFont);
    applyFontFamily(newFont);
  };

  return (
    <div className="flex items-center gap-2 px-3 py-1.5 text-xs rounded-full bg-zinc-100 dark:bg-zinc-800 border border-zinc-200 dark:border-zinc-700">
      <div className="flex items-center gap-1">
        <Palette className="w-3.5 h-3.5 text-zinc-500" />
        <button
          onClick={() => handleThemeChange('cream')}
          title="Kem dịu (Cream)"
          className={`px-1.5 py-0.5 rounded ${theme === 'cream' ? 'bg-amber-100 text-amber-900 font-bold' : 'text-zinc-600 dark:text-zinc-300'}`}
        >
          Cream
        </button>
        <button
          onClick={() => handleThemeChange('warm')}
          title="Ấm áp (Warm)"
          className={`px-1.5 py-0.5 rounded ${theme === 'warm' ? 'bg-amber-200 text-amber-950 font-bold' : 'text-zinc-600 dark:text-zinc-300'}`}
        >
          Warm
        </button>
        <button
          onClick={() => handleThemeChange('parchment')}
          title="Giấy cổ (Parchment)"
          className={`px-1.5 py-0.5 rounded ${theme === 'parchment' ? 'bg-yellow-100 text-yellow-900 font-bold' : 'text-zinc-600 dark:text-zinc-300'}`}
        >
          Parchment
        </button>
        <button
          onClick={() => handleThemeChange('mint')}
          title="Lá bạc hà (Mint)"
          className={`px-1.5 py-0.5 rounded ${theme === 'mint' ? 'bg-emerald-100 text-emerald-900 font-bold' : 'text-zinc-600 dark:text-zinc-300'}`}
        >
          Mint
        </button>
      </div>

      <span className="text-zinc-300 dark:text-zinc-600">|</span>

      <div className="flex items-center gap-1">
        <Type className="w-3.5 h-3.5 text-zinc-500" />
        <button
          onClick={() => handleSizeChange('sm')}
          className={`px-1.5 py-0.5 rounded ${fontSize === 'sm' ? 'bg-zinc-300 dark:bg-zinc-600 font-bold' : 'text-zinc-600 dark:text-zinc-300'}`}
        >
          A-
        </button>
        <button
          onClick={() => handleSizeChange('md')}
          className={`px-1.5 py-0.5 rounded ${fontSize === 'md' ? 'bg-zinc-300 dark:bg-zinc-600 font-bold' : 'text-zinc-600 dark:text-zinc-300'}`}
        >
          A
        </button>
        <button
          onClick={() => handleSizeChange('lg')}
          className={`px-1.5 py-0.5 rounded ${fontSize === 'lg' ? 'bg-zinc-300 dark:bg-zinc-600 font-bold' : 'text-zinc-600 dark:text-zinc-300'}`}
        >
          A+
        </button>
      </div>

      <span className="text-zinc-300 dark:text-zinc-600">|</span>

      <div className="flex items-center gap-1">
        <BookOpen className="w-3.5 h-3.5 text-zinc-500" />
        <button
          onClick={() => handleFontChange('serif')}
          className={`px-1.5 py-0.5 rounded font-serif ${fontFamily === 'serif' ? 'bg-zinc-300 dark:bg-zinc-600 font-bold' : 'text-zinc-600 dark:text-zinc-300'}`}
        >
          Lora
        </button>
        <button
          onClick={() => handleFontChange('sans')}
          className={`px-1.5 py-0.5 rounded font-sans ${fontFamily === 'sans' ? 'bg-zinc-300 dark:bg-zinc-600 font-bold' : 'text-zinc-600 dark:text-zinc-300'}`}
        >
          Inter
        </button>
      </div>
    </div>
  );
}
