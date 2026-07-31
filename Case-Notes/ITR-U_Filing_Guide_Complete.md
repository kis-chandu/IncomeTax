# ITR-U (UPDATED RETURN) FILING GUIDE
## AY 2025-26 | Chandrakant Gorai | PAN: ARQPG9033N

---

## 1. ELIGIBILITY CHECK ✅

| Condition | Status |
|---|---|
| Original return filed? | Yes (31-Jul-2025) |
| Within time limit (24 months from end of AY)? | Yes (deadline: 31-Mar-2028) |
| Results in additional tax (not increased refund)? | Yes ✅ |
| No search/survey/reassessment initiated? | Correct ✅ |
| No prosecution proceedings? | Correct ✅ |
| Filing within 12 months of end of AY? | Yes (AY ended 31-Mar-2026, filing in May/Jun 2026) → 25% additional tax |

**Key Rule:** ITR-U CANNOT be filed if it increases your refund. In your case, the correct VDA income (Rs.38,860) INCREASES your tax liability, which REDUCES your refund. This is permitted. ✅

---

## 2. ADDITIONAL TAX CALCULATION (Section 140B)

### Tax on Original Return:
```
Total Income:                    Rs.33,24,840
Tax at slab rates:               Rs.8,09,918
Tax on VDA @30% (Rs.113):        Rs.34
Total Tax:                       Rs.8,09,952
Surcharge:                       Rs.0
Cess @4%:                        Rs.32,398
Gross Tax Liability:             Rs.8,42,350
TDS:                             Rs.9,75,885
Refund:                          Rs.1,33,535 (+ Rs.7,343 interest = Rs.1,40,880 received)
```

### Tax on Updated Return:
```
Total Income:                    Rs.33,63,587 (33,24,840 + 38,747 additional VDA)
Tax at slab rates:               Rs.8,09,918 (unchanged — VDA taxed at special rate)
Tax on VDA @30% (Rs.38,860):     Rs.11,658
Total Tax:                       Rs.8,21,576
Surcharge:                       Rs.0
Cess @4%:                        Rs.32,863
Gross Tax Liability:             Rs.8,54,439
TDS:                             Rs.9,75,885
Refund (revised):                Rs.1,21,446
```

### Additional Tax Payable:
```
Revised Tax Liability:           Rs.8,54,439
Original Tax Liability:          Rs.8,42,350
─────────────────────────────────────────────
Additional Tax:                  Rs.12,089

Additional Tax u/s 140B @25%:    Rs.3,022
(within 12 months from end of AY 2025-26)

Interest u/s 234B:               Rs.0
(TDS Rs.9,75,885 > 90% of assessed tax Rs.8,54,439)

Interest u/s 234C:               Rs.0
(TDS deducted at source — no advance tax obligation)
─────────────────────────────────────────────
TOTAL TO PAY VIA CHALLAN:        Rs.15,111
(Round up to Rs.15,200 for safety)
```

---

## 3. STEP-BY-STEP FILING PROCESS

### STEP 1: Pay Self-Assessment Tax (Challan 280)

**MUST be done BEFORE filing ITR-U**

1. Login to https://eportal.incometax.gov.in
2. Go to **e-Pay Tax** → **New Payment**
3. Select **Income Tax** (not TDS/TCS)
4. Fill the challan:

| Field | Value |
|---|---|
| Tax Applicable | (0021) Income Tax (Other than Companies) |
| Type of Payment | (300) Self Assessment Tax |
| Assessment Year | 2025-26 |
| PAN | ARQPG9033N |
| Address | As per PAN records |
| Income Tax | Rs.12,089 |
| Surcharge | Rs.0 |
| Education Cess | Rs.0 |
| Other (Additional Tax u/s 140B) | Rs.3,022 |
| **Total** | **Rs.15,111** |

5. Pay via Net Banking / UPI / Debit Card
6. **SAVE THE RECEIPT** — Note down:
   - BSR Code
   - Challan Date
   - Challan Serial Number
   - Amount

---

### STEP 2: File ITR-U on the Portal

1. Login to https://eportal.incometax.gov.in
2. Go to **e-File** → **Income Tax Returns** → **File Income Tax Return**
3. Select:
   - Assessment Year: **2025-26**
   - Mode of Filing: **Online** (or Offline using JSON utility)
   - Filing Type: **Updated Return 139(8A)**
   - ITR Form: **ITR-2**

4. In the **Part A - General** section:
   - Return filed u/s: **139(8A)** — Updated Return
   - Original Return Ack No: **522131170310725**
   - Date of Original Return: **31/07/2025**
   - Reason for filing Updated Return: **Income not reported correctly**

---

### STEP 3: Fill Schedule VDA (Corrected)

Replace the 5 incorrect entries with these 6 consolidated entries (one per symbol):

| S.No | Date of Acquisition | Date of Transfer | Head | Cost of Acquisition (Rs.) | Consideration Received (Rs.) | Income from VDA (Rs.) |
|---|---|---|---|---|---|---|
| 1 | 2025-01-31 | 2025-03-31 | CG | 15,71,077 | 15,81,798 | 11,350 |
| 2 | 2025-01-31 | 2025-03-31 | CG | 5,67,600 | 5,70,522 | 4,414 |
| 3 | 2025-01-31 | 2025-03-31 | CG | 7,55,005 | 7,58,155 | 5,174 |
| 4 | 2025-01-31 | 2025-03-31 | CG | 23,18,643 | 23,29,163 | 17,910 |
| 5 | 2025-01-22 | 2025-01-22 | CG | 98 | 99 | 1 |
| 6 | 2025-01-22 | 2025-01-23 | CG | 100 | 111 | 11 |
| **TOTAL** | | | | **52,12,523** | **52,39,848** | **38,860** |

**Notes:**
- Entry 1 = BTC (consolidated)
- Entry 2 = ETH (consolidated)
- Entry 3 = SOL (consolidated)
- Entry 4 = XRP (consolidated)
- Entry 5 = USDT
- Entry 6 = VTHO
- "Income from VDA" = only positive gains (losses shown as 0 per Section 115BBH)
- Date of Acquisition = earliest buy date for that symbol
- Date of Transfer = last sell date for that symbol

---

### STEP 4: Key Sections to Update

#### Schedule CG (Capital Gains):
```
IncmFromVDATrnsf: 38,860 (was 113)
TotScheduleCGFor23: 38,860 (was 113)
```

#### Schedule SI (Special Income):
```
SecCode: 5BBH
SplRatePercent: 30
SplRateInc: 38,860 (was 113)
SplRateIncTax: 11,658 (was 34)
```

#### Part B-TI:
```
CapGains30Per115BBH: 38,860 (was 113)
TotalCapGains: 38,860 (was 113)
TotalTI: 39,47,090 (was 39,08,343)
GrossTotalIncome: 37,47,090 (was 37,08,343)
TotalIncome: 33,63,587 (was 33,24,840)
IncChargeableTaxSplRates: 38,860 (was 113)
```

#### Part B-TTI (Tax Computation):
```
TaxAtSpecialRates: 11,658 (was 34)
TaxPayableOnTotInc: 8,21,576 (was 8,09,952)
EducationCess: 32,863 (was 32,398)
GrossTaxLiability: 8,54,439 (was 8,42,350)
NetTaxLiability: 8,54,439 (was 8,42,350)
```

#### Schedule IT (Self Assessment Tax):
```
Add new entry:
  BSR Code: [from challan receipt]
  Date: [challan payment date]
  Serial No: [from challan receipt]
  Amount: Rs.15,111
```

#### TDS Schedules:
- **No change needed** — TDS entries remain the same (Rs.9,75,885 total)

---

### STEP 5: Verify and Submit

1. Validate the return — ensure no errors
2. The system will compute:
   - Revised refund: ~Rs.1,21,000 (approximately)
   - Since you already received Rs.1,40,880, the difference (~Rs.19,880) is what you're paying back via the challan + the reduced refund adjustment
3. Submit and e-Verify (Aadhaar OTP / Net Banking / DSC)

---

## 4. IMPORTANT NOTES

### On Consolidation of Schedule VDA:
- The IT portal allows multiple entries in Schedule VDA
- Consolidating 6,223 transactions into 6 symbol-wise entries is acceptable
- The CBDT has not mandated transaction-level reporting — symbol-level consolidation using FIFO is standard practice
- CoinSwitch's own tax report uses this approach

### On the 25% Additional Tax (Section 140B):
- This is NOT a penalty — it's a statutory additional tax for filing ITR-U
- It's calculated on the additional tax liability (Rs.12,089 × 25% = Rs.3,022)
- If you file after 12 months but within 24 months, it becomes 50%
- **File before 31-Mar-2027 to pay only 25%**

### On Refund Adjustment:
- Your original refund was Rs.1,40,880 (already received)
- Revised refund would be ~Rs.1,21,000
- The difference (~Rs.19,880) is covered by your challan payment of Rs.15,111 + the system will adjust
- You may receive a demand notice for the small difference, or it may be adjusted automatically

### Timeline:
- **Immediate:** Pay challan (Rs.15,111-15,200)
- **Within 1-2 weeks:** File ITR-U
- **No rush deadline** — you have until 31-Mar-2028 (but filing sooner = 25% vs 50% additional tax, and shows good faith after the 133(6) notice)

---

## 5. ALTERNATIVE: ENGAGE A CA

Given the complexity of ITR-U filing (it's a full ITR-2 re-submission), you may want to consider:

1. **Self-file on IT portal** — Use the online form, follow this guide
2. **Use ClearTax** — They support ITR-U filing; import your original return and modify
3. **Engage a CA** — Fee: Rs.1,500-3,000; they handle the entire filing

**My recommendation:** If you're comfortable with the IT portal, self-file using this guide. If not, a CA can do this in 30 minutes for a small fee. The key data (Schedule VDA entries, challan details) is all documented above.

---

## 6. DOCUMENTS TO KEEP READY

- [ ] Challan receipt (after payment)
- [ ] CoinSwitch Report (report_27477331.xlsx) — for Schedule VDA data
- [ ] Original ITR JSON (522131170310725.json) — to pre-fill unchanged sections
- [ ] PAN & Aadhaar — for e-verification
- [ ] Bank account details — for revised refund (if any)

---

## 7. AFTER FILING ITR-U

1. E-verify within 30 days
2. CPC will process the updated return
3. Since revised refund < original refund received, CPC may:
   - Adjust against the challan paid, OR
   - Issue a demand notice for the difference
4. If demand notice comes, pay it promptly
5. Keep all documents for 6 years (assessment can be reopened within this period)

---

*Document prepared: 20-May-2026*
*For: Chandrakant Gorai (PAN: ARQPG9033N)*
*Assessment Year: 2025-26*
