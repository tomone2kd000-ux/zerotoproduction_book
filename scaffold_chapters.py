import os
import json

docs_dir = r'E:\sach\zerotoproduction\content\docs'
os.makedirs(docs_dir, exist_ok=True)

chapters = [
    {
        'slug': 'mo-dau',
        'title': 'Mở Đầu: Zero To Production In Rust',
        'sections': [
            ('index.mdx', 'Mở Đầu: Giới Thiệu Cuốn Sách & Lời Tựa'),
            ('01-loi-tua-foreword.mdx', 'Lời Tựa (Foreword) - Lời Khuyên Từ Chuyên Gia'),
            ('02-loi-noi-dau-preface.mdx', 'Lời Nói Đầu (Preface) - Mục Tiêu & Đối Tượng Độc Giả')
        ]
    },
    {
        'slug': 'chuong-01-getting-started',
        'title': 'Chương 1: Bắt Đầu & Thiết Lập Toolchain',
        'sections': [
            ('index.mdx', 'Tổng Quan Chương 1: Getting Started'),
            ('01-cai-dat-rust-toolchain.mdx', '1.1 Cài Đặt Rust Toolchain Với Rustup'),
            ('02-khoi-tao-du-an-va-ide.mdx', '1.2 - 1.3 Thiết Lập Dự Án & Lựa Chọn IDE'),
            ('03-inner-development-loop-va-ci.mdx', '1.4 - 1.5 Vòng Lặp Phát Triển & Thiết Lập CI/CD')
        ]
    },
    {
        'slug': 'chuong-02-building-an-email-newsletter',
        'title': 'Chương 2: Thiết Kế Email Newsletter',
        'sections': [
            ('index.mdx', 'Tổng Quan Chương 2: Building An Email Newsletter'),
            ('01-vi-du-thuc-chien-va-user-stories.mdx', '2.1 - 2.2 Ví Dụ Thực Chiến & User Stories'),
            ('02-lam-viec-theo-iterations.mdx', '2.3 - 2.4 Phương Pháp Làm Việc Theo Iterations')
        ]
    },
    {
        'slug': 'chuong-03-sign-up-a-new-subscriber',
        'title': 'Chương 3: Đăng Ký Người Dùng Mới',
        'sections': [
            ('index.mdx', 'Tổng Quan Chương 3: Sign Up A New Subscriber'),
            ('01-chien-luoc-va-chon-web-framework.mdx', '3.1 - 3.2 Chiến Lược & Lựa Chọn Actix-web'),
            ('02-endpoint-health-check-va-kien-truc.mdx', '3.3 Endpoint Đầu Tiên: Health Check & Actix Anatomy'),
            ('03-integration-testing-thuc-chien.mdx', '3.4 - 3.6 Viết Integration Test Đầu Tiên'),
            ('04-xu-ly-html-forms-post-requests.mdx', '3.7 Xử Lý HTML Forms & POST Requests'),
            ('05-luu-tru-du-lieu-postgresql-sqlx.mdx', '3.8 Lưu Trữ Dữ Liệu: PostgreSQL & Crate SQLx'),
            ('06-persist-subscriber-va-app-state.mdx', '3.9 - 3.11 Lưu Subscriber, App State & Test Isolation')
        ]
    },
    {
        'slug': 'chuong-04-telemetry',
        'title': 'Chương 4: Giám Sát Từ Xa (Telemetry)',
        'sections': [
            ('index.mdx', 'Tổng Quan Chương 4: Telemetry & Observability'),
            ('01-quan-sat-he-thong-va-logging-co-ban.mdx', '4.1 - 4.3 Khả Năng Quan Sát & Logging Với Crate Log'),
            ('02-instrument-post-subscriptions.mdx', '4.4 Gắn Log & Truy Vết POST /subscriptions'),
            ('03-structured-logging-tracing-crate.mdx', '4.5 Structured Logging Với Crate Tracing & Spans'),
            ('04-bao-mat-secrets-va-request-id.mdx', '4.5.13 - 4.6 Bảo Mật Secrets, Request ID & Hệ Sinh Thái Tracing')
        ]
    },
    {
        'slug': 'chuong-05-going-live',
        'title': 'Chương 5: Triển Khai Production',
        'sections': [
            ('index.mdx', 'Tổng Quan Chương 5: Going Live'),
            ('01-chien-luoc-deployment-va-docker.mdx', '5.1 - 5.2 Chiến Lược Triển Khai & Ảo Hóa Docker'),
            ('02-xay-dung-dockerfile-toi-uu-va-sqlx.mdx', '5.3 Viết Dockerfile Tối Ưu, Cấu Hình & SQLx Offline Mode'),
            ('03-deploy-digitalocean-va-moi-truong.mdx', '5.4 Triển Khai DigitalOcean, Quản Lý Secrets & Biến Môi Trường')
        ]
    },
    {
        'slug': 'chuong-06-reject-invalid-subscribers-1',
        'title': 'Chương 6: Kiểm Tra Hợp Lệ #1 (Type-Driven)',
        'sections': [
            ('index.mdx', 'Tổng Quan Chương 6: Reject Invalid Subscribers #1'),
            ('01-yeu-cau-nghiep-vu-va-lo-hong-validation.mdx', '6.1 - 6.3 Yêu Cầu Nghiệp Vụ & Bài Học Validation'),
            ('02-type-driven-development-va-invariants.mdx', '6.4 - 6.6 Type-Driven Development & Invariants'),
            ('03-xu-ly-result-va-claims-assertions.mdx', '6.7 - 6.10 Biểu Diễn Lỗi Như Giá Trị: Result & Claims'),
            ('04-subscriber-email-va-property-based-testing.mdx', '6.11 - 6.15 SubscriberEmail & Property-based Testing (quickcheck)')
        ]
    },
    {
        'slug': 'chuong-07-reject-invalid-subscribers-2',
        'title': 'Chương 7: Kiểm Tra Hợp Lệ #2 (Email & Migrations)',
        'sections': [
            ('index.mdx', 'Tổng Quan Chương 7: Reject Invalid Subscribers #2'),
            ('01-xac-thuc-email-va-thiet-ke-emailclient.mdx', '7.1 - 7.2 Email Xác Thực & Thiết Kế EmailClient (Reqwest/WireMock)'),
            ('02-nguyen-tac-viet-test-suite-ben-vung.mdx', '7.3 - 7.4 Cấu Trúc Bộ Test Suite Dài Hạn & Maintainable'),
            ('03-zero-downtime-va-database-migrations.mdx', '7.5 - 7.6 Triển Khai Zero-Downtime & Multi-step Migrations'),
            ('04-gui-email-xac-thuc-va-tokens.mdx', '7.7 Gửi Email Xác Thực & Quản Lý Subscription Tokens'),
            ('05-database-transactions-trong-postgres-sqlx.mdx', '7.8 - 7.9 Giao Dịch Cơ Sở Dữ Liệu: Database Transactions Với SQLx')
        ]
    },
    {
        'slug': 'chuong-08-error-handling',
        'title': 'Chương 8: Xử Lý Lỗi Chuyên Nghiệp',
        'sections': [
            ('index.mdx', 'Tổng Quan Chương 8: Error Handling In Rust'),
            ('01-muc-dich-cua-loi-va-bao-cao-loi.mdx', '8.1 - 8.2 Mục Đích Của Lỗi & Error Trait Cho Operators'),
            ('02-dieu-khien-luong-va-thiserror.mdx', '8.3 Biểu Diễn Lỗi Bằng Enum & Loại Bỏ Boilerplate Với thiserror'),
            ('03-tranh-ball-of-mud-va-dung-anyhow.mdx', '8.4 - 8.6 Tránh Ball Of Mud, So Sánh anyhow vs thiserror')
        ]
    },
    {
        'slug': 'chuong-09-naive-newsletter-delivery',
        'title': 'Chương 9: Gửi Bản Tin Cơ Bản',
        'sections': [
            ('index.mdx', 'Tổng Quan Chương 9: Naive Newsletter Delivery'),
            ('01-user-stories-va-loc-subscribers.mdx', '9.1 - 9.3 Quy Trình Gửi Bản Tin & Lọc Subscriber Đã Xác Thực'),
            ('02-implementation-va-gui-newsletter.mdx', '9.4 - 9.7 Chiến Lược Triển Khai, Body Schema & Gửi Email'),
            ('03-gioi-han-cua-naive-approach.mdx', '9.8 - 9.10 Ranh Giới Trách Nhiệm & Giới Hạn Của Giải Pháp Cơ Bản')
        ]
    },
    {
        'slug': 'chuong-10-securing-our-api',
        'title': 'Chương 10: Bảo Mật & Xác Thực API',
        'sections': [
            ('index.mdx', 'Tổng Quan Chương 10: Securing Our API'),
            ('01-co-che-xac-thuc-va-password-auth.mdx', '10.1 - 10.4 Cơ Chế Xác Thực & Password Authentication (Argon2, TLS)'),
            ('02-login-forms-va-giao-dien-html.mdx', '10.5 - 10.6 Xử Lý Form Đăng Nhập & Phục Vụ Trang HTML'),
            ('03-session-based-auth-va-actix-session.mdx', '10.7 Quản Lý Phiên (Session-based Auth) Với Redis & actix-session'),
            ('04-seed-users-va-viet-actix-middleware.mdx', '10.8 - 10.10 Khởi Tạo Seed Users, Password Reset & Actix Middleware')
        ]
    },
    {
        'slug': 'chuong-11-fault-tolerant-workflows',
        'title': 'Chương 11: Luồng Chịu Lỗi & Tính Bất Biến',
        'sections': [
            ('index.mdx', 'Tổng Quan Chương 11: Fault-tolerant Workflows'),
            ('01-post-admin-newsletters-va-cac-failure-modes.mdx', '11.1 - 11.3 Ôn Lại POST /admin/newsletters & Các Loại Lỗi Hệ Thống'),
            ('02-khai-niem-idempotency-va-chia-khoa.mdx', '11.4 - 11.6 Khái Niệm Idempotency, Idempotency Keys & Chiến Lược'),
            ('03-idempotency-store-save-and-replay.mdx', '11.7 - 11.8 Lưu Trữ Trạng Thái: Idempotency Store & Cơ Chế Save-and-Replay'),
            ('04-concurrent-requests-va-recovery.mdx', '11.9 - 11.11 Xử Lý Request Đồng Thời, Forward/Backward Recovery & Lời Kết')
        ]
    }
]

# Master meta.json
master_pages = [
    'mo-dau',
    '--- PHẦN 1: BẮT ĐẦU VỚI RUST (FOUNDATIONS) ---',
    'chuong-01-getting-started',
    'chuong-02-building-an-email-newsletter',
    '--- PHẦN 2: XÂY DỰNG WEB SERVICE (CORE BACKEND) ---',
    'chuong-03-sign-up-a-new-subscriber',
    'chuong-04-telemetry',
    'chuong-05-going-live',
    '--- PHẦN 3: KIỂM SOÁT TÍNH HỢP LỆ & XỬ LÝ LỖI ---',
    'chuong-06-reject-invalid-subscribers-1',
    'chuong-07-reject-invalid-subscribers-2',
    'chuong-08-error-handling',
    '--- PHẦN 4: HỆ THỐNG NÂNG CAO & AN TOÀN TRƯỚC LỖI ---',
    'chuong-09-naive-newsletter-delivery',
    'chuong-10-securing-our-api',
    'chuong-11-fault-tolerant-workflows'
]

with open(os.path.join(docs_dir, 'meta.json'), 'w', encoding='utf-8') as f:
    json.dump({'title': 'Zero To Production In Rust', 'pages': master_pages}, f, indent=2, ensure_ascii=False)

for ch in chapters:
    ch_dir = os.path.join(docs_dir, ch['slug'])
    os.makedirs(ch_dir, exist_ok=True)
    
    pages = [s[0].replace('.mdx', '') for s in ch['sections']]
    with open(os.path.join(ch_dir, 'meta.json'), 'w', encoding='utf-8') as f:
        json.dump({'title': ch['title'], 'pages': pages}, f, indent=2, ensure_ascii=False)
        
    for fname, title in ch['sections']:
        fpath = os.path.join(ch_dir, fname)
        if not os.path.exists(fpath):
            with open(fpath, 'w', encoding='utf-8') as f:
                f.write(f'''---
title: "{title}"
description: "Tài liệu chi tiết thuộc {ch['title']}"
---

# {title}

<Callout type="info">
  Đang cập nhật nội dung biên soạn chuyên sâu...
</Callout>
''')

print('Scaffold completed successfully!')
