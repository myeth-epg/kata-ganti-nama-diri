-- =====================================================================
-- Kata Ganti Nama Diri (iflow-edugames-kata-ganti-nama-diri) Supabase Tables
-- Keeps existing public.students shared across BM, English & KGND games,
-- while separating KGND quiz records, quizzes, and assignments.
-- =====================================================================

-- 1. KGND Quiz History
create table if not exists public.quiz_history_kgnd (
  id uuid default gen_random_uuid() primary key,
  student_id uuid references public.students(id),
  username text,
  display_name text,
  category text,
  score_correct int default 0,
  score_wrong int default 0,
  total_questions int default 20,
  accuracy int default 0,
  duration_seconds int default 0,
  wrong_words jsonb default '[]'::jsonb,
  played_at timestamptz default now()
);

alter table public.quiz_history_kgnd enable row level security;
create policy "Allow public read quiz_history_kgnd" on public.quiz_history_kgnd for select using (true);
create policy "Allow public insert quiz_history_kgnd" on public.quiz_history_kgnd for insert with check (true);
create policy "Allow public update quiz_history_kgnd" on public.quiz_history_kgnd for update using (true);

-- 2. KGND Teacher-Created Quizzes
create table if not exists public.quizzes_kgnd (
  id uuid default gen_random_uuid() primary key,
  quiz_code text unique not null,
  title text default '',
  units jsonb default '[]'::jsonb,
  question_ids jsonb default '[]'::jsonb,
  question_count int default 20,
  is_archived boolean not null default false,
  created_at timestamptz default now()
);
alter table public.quizzes_kgnd add column if not exists is_archived boolean not null default false;

alter table public.quizzes_kgnd enable row level security;
create policy "Allow public read quizzes_kgnd" on public.quizzes_kgnd for select using (true);
create policy "Allow public insert quizzes_kgnd" on public.quizzes_kgnd for insert with check (true);
create policy "Allow public update quizzes_kgnd" on public.quizzes_kgnd for update using (true);
create policy "Allow public delete quizzes_kgnd" on public.quizzes_kgnd for delete using (true);

-- 3. KGND Quiz Assignments
create table if not exists public.quiz_assignments_kgnd (
  id uuid default gen_random_uuid() primary key,
  quiz_id uuid references public.quizzes_kgnd(id) on delete cascade,
  quiz_code text not null,
  student_id uuid references public.students(id) on delete cascade,
  username text,
  display_name text,
  status text default 'pending',
  attempt_no int default 1,
  score_correct int,
  score_wrong int,
  accuracy int,
  assigned_at timestamptz default now(),
  completed_at timestamptz
);

alter table public.quiz_assignments_kgnd enable row level security;
create policy "Allow public read quiz_assignments_kgnd" on public.quiz_assignments_kgnd for select using (true);
create policy "Allow public insert quiz_assignments_kgnd" on public.quiz_assignments_kgnd for insert with check (true);
create policy "Allow public update quiz_assignments_kgnd" on public.quiz_assignments_kgnd for update using (true);
create policy "Allow public delete quiz_assignments_kgnd" on public.quiz_assignments_kgnd for delete using (true);

-- 4. Forced Resume State for Kata Ganti Nama Diri (separate from BM & English)
alter table public.students add column if not exists active_quiz_state_kgnd jsonb default null;
