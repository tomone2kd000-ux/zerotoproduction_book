import Link from 'next/link';
import { BookOpen, ShieldCheck, Server, Terminal, ArrowRight, Sparkles, Cpu, Layers } from 'lucide-react';

export default function HomePage() {
  return (
    <div className="min-h-screen bg-zinc-50/50 dark:bg-zinc-950 text-zinc-900 dark:text-zinc-100 flex flex-col font-sans">
      {/* Header Navigation */}
      <header className="border-b border-zinc-200/80 dark:border-zinc-800/80 bg-white/70 dark:bg-zinc-900/70 backdrop-blur-md sticky top-0 z-50">
        <div className="max-w-6xl mx-auto px-6 h-16 flex items-center justify-between">
          <div className="flex items-center gap-3">
            <div className="w-9 h-9 rounded-xl bg-orange-500/10 border border-orange-500/30 flex items-center justify-center text-orange-600 dark:text-orange-400 font-bold">
              <Cpu className="w-5 h-5" />
            </div>
            <span className="font-bold text-lg tracking-tight font-serif">Zero To Production In Rust</span>
          </div>
          <Link
            href="/docs/mo-dau"
            className="inline-flex items-center gap-2 px-4 py-2 text-sm font-medium rounded-full bg-zinc-900 dark:bg-zinc-100 text-white dark:text-zinc-900 hover:bg-zinc-800 dark:hover:bg-zinc-200 transition-colors shadow-sm"
          >
            <BookOpen className="w-4 h-4" />
            Đọc Sách Ngay
          </Link>
        </div>
      </header>

      {/* Hero Section */}
      <main className="flex-1 max-w-6xl mx-auto px-6 py-12 md:py-20">
        <div className="grid grid-cols-1 md:grid-cols-12 gap-12 items-center">
          <div className="md:col-span-7 space-y-6">
            <div className="inline-flex items-center gap-2 px-3 py-1 rounded-full text-xs font-semibold bg-orange-100 dark:bg-orange-950/60 text-orange-800 dark:text-orange-300 border border-orange-200 dark:border-orange-800/60">
              <Sparkles className="w-3.5 h-3.5" />
              Cloud-Native Web Development in Rust
            </div>
            <h1 className="text-4xl md:text-5xl font-extrabold tracking-tight font-serif leading-tight">
              Phát Triển Web Service Chuyên Nghiệp Bằng Rust
            </h1>
            <p className="text-lg text-zinc-600 dark:text-zinc-400 leading-relaxed">
              Từ một dự án trống trơn đến một dịch vụ backend sẵn sàng chạy Production. Cuốn sách kinh điển của <strong>Luca Palmieri</strong> hướng dẫn chi tiết về Actix-web, SQLx, Docker, Telemetry, Type-Driven Development và Idempotency.
            </p>

            <div className="pt-4 flex flex-wrap items-center gap-4">
              <Link
                href="/docs/mo-dau"
                className="inline-flex items-center gap-2 px-6 py-3 text-base font-semibold rounded-xl bg-orange-600 hover:bg-orange-700 text-white transition-all shadow-md shadow-orange-600/20"
              >
                Khám Phá Sơ Đồ Chương Mục
                <ArrowRight className="w-4 h-4" />
              </Link>
            </div>
          </div>

          {/* Book Cover Container */}
          <div className="md:col-span-5 flex justify-center">
            <div className="relative group w-full max-w-md">
              <div className="absolute -inset-1 bg-gradient-to-r from-orange-500 to-amber-500 rounded-2xl blur opacity-30 group-hover:opacity-50 transition duration-1000 group-hover:duration-200"></div>
              <div className="relative w-full aspect-[3/4] max-h-[460px] rounded-2xl bg-zinc-900 border border-zinc-800 shadow-2xl overflow-hidden flex items-center justify-center">
                <img
                  src="/cover.jpeg"
                  alt="Zero To Production In Rust Cover"
                  className="w-full h-full object-contain transition-transform duration-500 group-hover:scale-105"
                />
              </div>
            </div>
          </div>
        </div>

        {/* 4 Parts Grid */}
        <section className="mt-20 pt-16 border-t border-zinc-200 dark:border-zinc-800">
          <div className="text-center max-w-2xl mx-auto mb-12">
            <h2 className="text-2xl md:text-3xl font-bold font-serif">4 Phần & 11 Chương Thực Chiến Toàn Diện</h2>
            <p className="text-sm text-zinc-600 dark:text-zinc-400 mt-2">
              Hệ thống hóa toàn bộ kiến trúc ứng dụng Email Newsletter từ con số 0 đến môi trường Production.
            </p>
          </div>

          <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-6">
            {/* Part 1 */}
            <div className="p-6 rounded-2xl bg-white dark:bg-zinc-900 border border-zinc-200 dark:border-zinc-800 space-y-4 hover:border-orange-500/50 transition-colors">
              <div className="w-10 h-10 rounded-xl bg-blue-500/10 text-blue-600 dark:text-blue-400 flex items-center justify-center font-bold">
                <Terminal className="w-5 h-5" />
              </div>
              <h3 className="text-lg font-bold">Phần 1: Bắt Đầu Với Rust</h3>
              <p className="text-xs text-zinc-500 leading-relaxed">
                Cài đặt Rustup, lựa chọn Toolchain, tối ưu Inner Development Loop và thiết lập CI/CD tự động.
              </p>
              <span className="text-xs font-semibold text-blue-600 dark:text-blue-400 block">Chương 1 - 2</span>
            </div>

            {/* Part 2 */}
            <div className="p-6 rounded-2xl bg-white dark:bg-zinc-900 border border-zinc-200 dark:border-zinc-800 space-y-4 hover:border-orange-500/50 transition-colors">
              <div className="w-10 h-10 rounded-xl bg-orange-500/10 text-orange-600 dark:text-orange-400 flex items-center justify-center font-bold">
                <Server className="w-5 h-5" />
              </div>
              <h3 className="text-lg font-bold">Phần 2: Xây Dựng Web Service</h3>
              <p className="text-xs text-zinc-500 leading-relaxed">
                Actix-web, PostgreSQL & SQLx, Observability với tracing/spans, đóng gói Docker và deploy DigitalOcean.
              </p>
              <span className="text-xs font-semibold text-orange-600 dark:text-orange-400 block">Chương 3 - 5</span>
            </div>

            {/* Part 3 */}
            <div className="p-6 rounded-2xl bg-white dark:bg-zinc-900 border border-zinc-200 dark:border-zinc-800 space-y-4 hover:border-orange-500/50 transition-colors">
              <div className="w-10 h-10 rounded-xl bg-emerald-500/10 text-emerald-600 dark:text-emerald-400 flex items-center justify-center font-bold">
                <ShieldCheck className="w-5 h-5" />
              </div>
              <h3 className="text-lg font-bold">Phần 3: Kiểm Soát Tính Hợp Lệ & Lỗi</h3>
              <p className="text-xs text-zinc-500 leading-relaxed">
                Type-Driven Development, Property-based testing, WireMock, Zero-downtime migrations và thiserror/anyhow.
              </p>
              <span className="text-xs font-semibold text-emerald-600 dark:text-emerald-400 block">Chương 6 - 8</span>
            </div>

            {/* Part 4 */}
            <div className="p-6 rounded-2xl bg-white dark:bg-zinc-900 border border-zinc-200 dark:border-zinc-800 space-y-4 hover:border-orange-500/50 transition-colors">
              <div className="w-10 h-10 rounded-xl bg-purple-500/10 text-purple-600 dark:text-purple-400 flex items-center justify-center font-bold">
                <Layers className="w-5 h-5" />
              </div>
              <h3 className="text-lg font-bold">Phần 4: Hệ Thống Chịu Lỗi & Bảo Mật</h3>
              <p className="text-xs text-zinc-500 leading-relaxed">
                Bảo mật API, Password hashing (Argon2), Session-based Auth và luồng xử lý chịu lỗi Idempotency.
              </p>
              <span className="text-xs font-semibold text-purple-600 dark:text-purple-400 block">Chương 9 - 11</span>
            </div>
          </div>
        </section>
      </main>

      {/* Footer */}
      <footer className="border-t border-zinc-200 dark:border-zinc-800 py-8 text-center text-xs text-zinc-500">
        <p>© 2026 Zero To Production In Rust • Luca Palmieri • Fumadocs Web Docs</p>
      </footer>
    </div>
  );
}
