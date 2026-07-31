# Tax Computation Worksheet — FY 2025-26 (AY 2026-27) — FILLED
*Source documents (read 29 Jul 2026): Form 16 Part A (RSRYFJA), Form 16 Part B, HDFC interest cert (loan 703764316), employer tax computation (Mercans).*

## Extracted inputs (verified against documents)
| Item | Value |
|---|---|
| Employer | TechAspect Solutions Pvt Ltd, Hyderabad — TDS fully deposited (OLTAS status F) |
| Regime used by employer | **OLD** (Part B: "opting out of 115BAC(1A)? Yes") — NOT binding at filing |
| Gross salary 17(1) | ₹41,87,293 |
| Exemptions u/s 10 applied by employer | ₹26,400 (food allowance) |
| Professional tax | ₹2,400 |
| TDS deducted (salary) | **₹9,62,050** |
| Home loan (₹42.5L @7.60%, HDFC, Kadugodi Bengaluru; co-borrower: wife Priyanka) | FY25-26: EMI ₹1,81,304 (₹74,230 principal + ₹1,07,074 interest) + **pre-EMI interest ₹2,26,961**; EMIs began Dec-2025 |
| 80C declared | ₹1,50,000 (cap hit; gross decl. ₹2,38,612) |
| 80CCD(1B) NPS own | ₹50,000 |
| 80CCD(2) NPS employer | ₹0 — **MAJOR missed lever (see playbook)** |
| 80D declared to employer | ₹0 (client has premiums — parents >60 — unclaimed at payroll; matters only if old regime) |
| Basic salary (annual) | ₹16,97,013 → 80CCD(2) capacity 14% = **₹2,37,582/yr** |
| House | self-occupied (no rent) |
| Savings interest | pending (client to confirm via AIS) |

## A. OLD REGIME (as employer computed — reconstructed, exact match)
Gross 41,87,293 − 10-exempt 26,400 − std ded 50,000 − PT 2,400 = 41,08,493 (Salaries)
Less 24(b) self-occupied interest (capped) **2,00,000** → GTI 39,08,493
Less VI-A: 80C 1,50,000 + 80CCD(1B) 50,000 = 2,00,000 → **TI = 37,08,493**
Tax: 12,500 + 1,00,000 + 30%×27,08,493 = 9,25,048 | Cess 37,002 | **Total ₹9,62,050** ✔ (= TDS, ₹0 refund/due)
*Even adding 80D ₹75k + 80TTA ₹10k: TI ≈36,23,493 → tax ≈9,07,246+cess ≈ ₹9,43,500 → still ~₹97k WORSE than new regime.*

## B. NEW REGIME (115BAC default) — recommended
Gross 41,87,293 − std ded **75,000** = 41,12,293 (no 10-exemptions [food taxable], no PT, no 24(b) loss, no VI-A except 80CCD(2)=0)
Slabs: 0-4L 0 | 4-8 20,000 | 8-12 40,000 | 12-16 60,000 | 16-20 80,000 | 20-24 1,00,000 | >24L: 30%×17,12,293 = 5,13,688
Slab tax = **8,13,688** | 87A: NA (>12L) | Surcharge: nil (<50L) | Cess 4% = 32,548
**Total tax = ₹8,46,236** (± small change for SB interest @ ~31.2% of interest amt)

## C. VERDICT
**New regime cheaper by ₹1,15,814** → since TDS ₹9,62,050 already deducted: **REFUND ≈ ₹1,15,814** (gross of SB-interest tax, e.g., interest ₹15k → refund ≈ ₹1.11L).
Decision robust: old regime cannot catch up even with 80D+80TTA+80EEA stacked.

## Remaining input before filing
1. **AIS + TIS + 26AS figures** (client will pull on portal login): SB interest, **bond interest (Wintwealth, TDS u/s 193 @10%)**, any MF dividends (194K). *Client revealed 29-Jul: holds MFs + bonds via Wintwealth, no redemptions claimed.*
2. **Confirm ZERO capital-gain events**: no MF switches (switch=taxable redemption!), no bond maturity/call/SWP in FY25-26. If any → add CG schedule (ITR-1 still OK if only 112A ≤₹1.25L).
3. 80D: employer group mediclaim DEDUCTED from HIS salary (employee-paid → eligible) covering wife+kid+parents(>60); max ₹75k. **Resolved: unusable in new regime; even ₹75k credit to old loses by ~₹97k. Not claimed this year.** Get exact premium from payslip for records.
4. (Optional family play) Wife's ownership share + whether she has taxable income (see playbook §4).

# Tax Computation Worksheet — FY 2025-26 (AY 2026-27) — FINAL ✔ FILING-READY
*29 Jul 2026: AIS/26AS prefill (ClearTax fetch) received. All cross-checks pass. No surprise capital gains → ITR-1 confirmed.*

## Income heads (verified: Form 16 ✔ + AIS ✔)
| Source | Amount | Note |
|---|---|---|
| Salary 17(1) | ₹41,87,293 | matches Form 16 |
| C1 Savings interest | ₹6,117 | |
| C2 FD interest | ₹10,894 | ⚠ client believed "no FD" — AIS says otherwise (auto-sweep/deposit interest). Taxable regardless. |
| C3 Refund interest (prev yr) | ₹7,343 | classic missed item — taxable IFOS |
| E1 Other sources | ₹20,241 | bond interest (Wintwealth) |
| D1 Dividends (domestic) | ₹10,898 | stocks/IDCW per AIS |
| **TDS credits** | **₹9,65,057** | salary 9,62,050 + others ~3,007 — ALL claimable |

## FINAL — NEW REGIME (selected)
TI = 41,87,293 − 75,000 + 55,493 = **₹41,67,786** (rounds 41,67,790)
Tax: 3,00,000 (≤24L) + 30% × 17,67,790 = 8,30,337 | Cess 33,213 | **Total = ₹8,63,550**
234B/234C interest: **NIL** (TDS 9,65,057 > total tax)
**REFUND = 9,65,057 − 8,63,550 ≈ ₹1,01,507 (±₹10 rounding)**

## Cross-check — OLD REGIME with MAX deductions (80C 1.5L + NPS 50k + 24(b) 2L + 80D max 75k + 80TTA 6,117 + food 26,400 + PT 2,400)
TI = 36,82,870 → tax 9,17,361 + cess 36,694 = **₹9,54,055**
**NEW wins by ₹90,505 — verdict final.** (80D unknowable → maxed; still loses.)

## ClearTax screen note
"Taxes Paid ₹9,65,057" matches TDS credits. Their "Tax Savings ₹75,000" is a UI artifact (likely std deduction/deduction finder) — immaterial to math. Any platform's lawful max refund can only be ₹1,01,507 on this data.

## FINAL LEDGER — AY 2026-27 (locked 30-Jul-2026, post-Univest discovery)
Normal-rate income: Salary 41,12,293 + IFOS 56,153 + STCG +1,729.41 (Univest +3,063.96, Zerodha -462.55, MF -872) - Business loss 30,741.78 (F&O -30,760.28 net of charges 3,250.53; spec +18.50) = 41,39,433.63 → 41,39,430.
Special: 112A LTCG 7,766.40 exempt (≤1.25L) | VDA 750.05 @30% = 225.
Tax: 8,21,829 (slab new regime) + 225 + cess 32,882 = **8,54,940**.
TDS: **9,64,913** (26AS) → **REFUND ₹1,09,973**.
Interest 234A/B/C: NIL. Carry-forward: NIL. Audit 44AB: NO. Form: ITR-3. Regime: NEW.
