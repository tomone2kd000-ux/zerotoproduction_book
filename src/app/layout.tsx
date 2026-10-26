import './global.css';
import { RootProvider } from 'fumadocs-ui/provider/next';
import { Inter, Lora } from 'next/font/google';
import type { ReactNode } from 'react';

const inter = Inter({ subsets: ['latin'], variable: '--font-sans' });
const lora = Lora({ subsets: ['latin', 'vietnamese'], variable: '--font-serif' });

export default function Layout({ children }: { children: ReactNode }) {
  return (
    <html lang="vi" className={`${inter.variable} ${lora.variable} ${inter.className}`} suppressHydrationWarning>
      <body className="flex flex-col min-h-screen">
        <RootProvider>{children}</RootProvider>
      </body>
    </html>
  );
}
