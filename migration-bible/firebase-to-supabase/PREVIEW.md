# AST Surgery Preview: Firebase → Supabase

> **⚡ This transformation took 0.2 seconds of AST Surgery by Forjet Engine.**

---

## 1. Authentication: `firebase.auth()` → `supabase.auth`

```diff
// BEFORE (Firebase)
- import { getAuth, signInWithEmailAndPassword, onAuthStateChanged } from 'firebase/auth';
- import { initializeApp } from 'firebase/app';
-
- const app = initializeApp(firebaseConfig);
- const auth = getAuth(app);
-
- // Sign in
- await signInWithEmailAndPassword(auth, email, password);
-
- // Get current user
- onAuthStateChanged(auth, (user) => {
-   if (user) {
-     console.log('User UID:', user.uid); // string UID
-   }
- });

// AFTER (Supabase)
+ import { createClient } from '@supabase/supabase-js';
+
+ const supabase = createClient(
+   process.env.NEXT_PUBLIC_SUPABASE_URL!,
+   process.env.NEXT_PUBLIC_SUPABASE_ANON_KEY!
+ );
+
+ // Sign in
+ await supabase.auth.signInWithPassword({ email, password });
+
+ // Get current user
+ const { data: { subscription } } = supabase.auth.onAuthStateChange((event, session) => {
+   if (session?.user) {
+     console.log('User UUID:', session.user.id); // UUID
+   }
+ });
```

---

## 2. Database Queries: Firestore → Supabase Postgres

```diff
// BEFORE (Firestore)
- import { getFirestore, collection, doc, getDocs, addDoc, query, where } from 'firebase/firestore';
-
- const db = getFirestore(app);
-
- // Fetch all posts by a user
- const q = query(collection(db, 'posts'), where('userId', '==', userId));
- const snapshot = await getDocs(q);
- const posts = snapshot.docs.map(doc => ({ id: doc.id, ...doc.data() }));
-
- // Insert a new post
- await addDoc(collection(db, 'posts'), {
-   title: 'Hello World',
-   userId: auth.currentUser.uid,
-   createdAt: serverTimestamp(),
- });

// AFTER (Supabase)
+ import { supabase } from '@/lib/supabase';
+
+ // Fetch all posts by a user (with JOIN support!)
+ const { data: posts, error } = await supabase
+   .from('posts')
+   .select('*, users(name, avatar_url)')  // ← Firestore CAN'T do this
+   .eq('user_id', session.user.id)
+   .order('created_at', { ascending: false });
+
+ // Insert a new post
+ const { data, error } = await supabase
+   .from('posts')
+   .insert({
+     title: 'Hello World',
+     user_id: session.user.id,
+   })
+   .select()
+   .single();
```

---

## 3. Real-time Subscriptions: `onSnapshot` → `supabase.channel`

```diff
// BEFORE (Firestore)
- import { onSnapshot, collection, query, where } from 'firebase/firestore';
-
- const q = query(collection(db, 'messages'), where('roomId', '==', roomId));
- const unsubscribe = onSnapshot(q, (snapshot) => {
-   snapshot.docChanges().forEach((change) => {
-     if (change.type === 'added') setMessages(prev => [...prev, change.doc.data()]);
-   });
- });

// AFTER (Supabase Realtime)
+ const channel = supabase
+   .channel(`room:${roomId}`)
+   .on(
+     'postgres_changes',
+     { event: 'INSERT', schema: 'public', table: 'messages', filter: `room_id=eq.${roomId}` },
+     (payload) => setMessages(prev => [...prev, payload.new])
+   )
+   .subscribe();
+
+ // Cleanup
+ return () => supabase.removeChannel(channel);
```

---

## 4. Storage: Firebase Storage → Supabase Storage

```diff
// BEFORE (Firebase Storage)
- import { getStorage, ref, uploadBytes, getDownloadURL, deleteObject } from 'firebase/storage';
-
- const storage = getStorage(app);
- const storageRef = ref(storage, `avatars/${userId}.jpg`);
- await uploadBytes(storageRef, file);
- const url = await getDownloadURL(storageRef);

// AFTER (Supabase Storage)
+ const { data, error } = await supabase.storage
+   .from('avatars')
+   .upload(`${userId}.jpg`, file, { upsert: true });
+
+ const { data: { publicUrl } } = supabase.storage
+   .from('avatars')
+   .getPublicUrl(`${userId}.jpg`);
```

---

## 5. Environment Variables

```diff
# .env.local — BEFORE
- FIREBASE_API_KEY=AIzaSyXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
- FIREBASE_AUTH_DOMAIN=your-app.firebaseapp.com
- FIREBASE_PROJECT_ID=your-app-12345
- FIREBASE_STORAGE_BUCKET=your-app.appspot.com
- FIREBASE_MESSAGING_SENDER_ID=123456789
- FIREBASE_APP_ID=1:123456789:web:abcdefabcdef

# .env.local — AFTER
+ NEXT_PUBLIC_SUPABASE_URL=https://xxxx.supabase.co
+ NEXT_PUBLIC_SUPABASE_ANON_KEY=eyJhbGci...
+ SUPABASE_SERVICE_ROLE_KEY=eyJhbGci...
```

---

> **⚡ This took 0.2 seconds of AST Surgery. It would have taken you 2–3 days manually.**
>
> *Generated and validated by [Forjet Engine](https://forjet.dev).*
