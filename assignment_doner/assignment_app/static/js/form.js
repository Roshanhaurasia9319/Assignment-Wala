

  document.addEventListener('DOMContentLoaded', function () {
    
      var workType = document.getElementById("WorkType");
      var sheet = document.getElementById("Sheet");
      var amount = document.getElementById("amount");
      function calculateAmount() {
          var workTypeValue = workType.value;
          var sheetValue = parseInt(sheet.value);

          if (workTypeValue == "Assignment") {
              amount.innerHTML = sheetValue * 5 + "Rs";
          } else {
              amount.innerHTML = sheetValue * 50 + "Rs";
          }
      }

      workType.addEventListener('change', calculateAmount);
      sheet.addEventListener('input', calculateAmount);

      // Initial calculation
      calculateAmount();
  });

