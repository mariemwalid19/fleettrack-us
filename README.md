# FleetTrack US

## One-line goal
Allow dispatchers to assign loads and watch drivers’ live locations across the United States; drivers can accept jobs, chat, and upload proof-of-delivery.

## Owner
Mariem Walid

---

## Target platforms
Responsive web app + PWA (works on laptop and phone). Later we can add native apps if needed.

## Primary users / roles
- Drivers (US)
- Dispatchers (office)
- Admin

## MVP (must-have features)
1. Driver login and assignment inbox (assigned loads visible).
2. Dispatcher dashboard with live map showing drivers (updates ~10–15s).
3. Driver can Accept / Decline an assigned load.
4. In-app chat (text, photos, location) between driver and dispatcher.
5. Upload Proof-of-Delivery (photo + geotag).
6. Push notifications for new assignments (FCM / APNs).
7. Basic audit trail (timestamps for assignment status changes).

## Nice-to-have (post-MVP)
- Auto-assign nearest driver
- Route optimization
- Signature capture
- Advanced analytics and reports

## Geographic scope / constraints
United States only. Use a map provider with full US coverage (Mapbox or Google Maps).

## Non-functional requirements
- HTTPS everywhere.
- JWT-based auth.
- Location update interval configurable (10–15s while active).
- Keep last 30 days of location history (configurable).

## Legal / privacy notes
- Must include explicit background-location consent flow and a privacy policy explaining why "always-on" location is needed for deliveries.
- Prepare App Store / Play Store justifications if we later add native apps.

## Success metrics (initial)
- Dispatcher sees driver update within 15s 95% of the time during beta.
- Drivers can accept and complete assigned loads with POD uploads in >90% of trips.

## Initial tech stack (suggested)
- Frontend: React (PWA via Create React App or Next.js).
- Backend: Flask + Flask-SocketIO (or Firebase for faster prototyping).
- Database: Postgres + PostGIS (location support).
- Realtime: Socket.IO (or Firebase Realtime).
- Maps: Mapbox (or Google Maps).
- Storage: AWS S3 or equivalent for photos.
- Hosting: Cloud Run / Vercel / DigitalOcean.

## Accounts to create (first)
1. GitHub (repo)
2. Mapbox (or Google Cloud account)
3. Firebase (for FCM / quick prototyping) or cloud provider (GCP/AWS)
4. Apple Developer & Google Play Console (only if building native apps)

## First milestone (deliverable)
**Working responsive dashboard showing one driver’s live location (simulated GPS points) on a US map.**
Target: 2 weeks

---

## First concrete steps (what to do next)
1. Create GitHub repo named `fleettrack-us`.  
2. Add this `README.md` as the repository README.  
3. Push the repo to GitHub and share the link with your developer or paste it back here.

---

## Contact / Owner
Mariem Walid
